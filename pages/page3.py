from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from data import df


def create_population_graph(filtered_df):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=filtered_df['municipality'], y=filtered_df['population']))
    fig.update_layout(title_text='Численность населения региона')
    return fig

def create_income_over_years_graph(filtered_df):
    # Группируем данные по годам и суммируем доход
    grouped_df = filtered_df.groupby('year')['income'].sum().reset_index()

    # Создаем линейный график
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=grouped_df['year'], y=grouped_df['income'], mode='lines'))
    fig.update_layout(title_text='Сумма дохода региона за несколько лет')
    return fig

def page3(region):
    filtered_df = df[(df['region'] == region)]
    layout = html.Div([
         dbc.Row([
            dbc.Col(dcc.Graph(figure=create_population_graph(filtered_df)), width=5, style={'border': 'solid 2px', 'border-radius': '20px', 'margin': '15px', 'width': '120vh', 'height' : '100hv'}), 
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(figure=create_income_over_years_graph(filtered_df)), width=5, style={'border': 'solid 2px', 'border-radius': '20px', 'margin': '15px','width': '120vh', 'height' : '100hv'})
        ]),
    ], style={'margin': '15px', 'padding-top': '10%'})
    return layout

layout = dbc.Container([
    dbc.Row([
        dcc.Dropdown(
            options=[{'label': region, 'value': region} for region in df['region'].unique()],
            value=df['region'].unique()[0],
            id='region-dropdown'
        ),
    ]),
    dbc.Row([
        html.Div(id='page-3-graph-container')
    ])
    
])



@callback(
    Output('page-3-graph-container', 'children'),
    Input('region-dropdown', 'value')
)
def update_page_1(region):
    return page3(region)