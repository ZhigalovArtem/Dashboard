from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from data import df


def create_population_graph(filtered_df):
    grouped_df = filtered_df.groupby('municipality')['population'].sum().reset_index()
    fig = go.Figure()
    fig.add_trace(go.Bar(x=grouped_df['municipality'], y=grouped_df['population']))
    fig.update_layout(title_text='Численность населения муниципальных районов', paper_bgcolor='#AF947F', plot_bgcolor='#AF947F')
    return fig

def create_income_over_years_graph(filtered_df):
    # Группируем данные по годам и суммируем доход
    grouped_df = filtered_df.groupby('year')['income'].sum().reset_index()

    # Создаем линейный график
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=grouped_df['year'], y=grouped_df['income'], mode='lines'))
    fig.update_layout(title_text='График дохода региона', paper_bgcolor='#AF947F', plot_bgcolor='#AF947F')
    return fig

def page3(region, year):
    filtered_df_region = df[(df['region'] == region)]
    filtered_df = df[(df['region'] == region) & (df['year'] == year)]

    layout = html.Div([
         dbc.Row([
            dbc.Col(dcc.Graph(figure=create_population_graph(filtered_df)), width=5, style={'border': 'solid 2px', 'border-radius': '20px', 'margin': '15px', 'width': '120vh', 'height' : '100hv'}), 
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(figure=create_income_over_years_graph(filtered_df_region)), width=5, style={'border': 'solid 2px', 'border-radius': '20px', 'margin': '15px','width': '120vh', 'height' : '100hv'})
        ]),
    ], style={'margin': '15px'})
    return layout

layout = dbc.Container([
    dbc.Row([
        dcc.Dropdown(
            options=[{'label': region, 'value': region} for region in df['region'].unique()],
            value=df['region'].unique()[5],
            id='region-dropdown',
            style={'margin-bottom':'2px'}
        ),
        dcc.Dropdown(
            options=[{'label': year, 'value': year} for year in df['year'].sort_values().unique()],
            value=2012,
            id='year-dropdown'
        )
    ]),
    dbc.Row([
        html.Div(id='page-3-graph-container')
    ])
    
])



@callback(
    Output('page-3-graph-container', 'children'),
    Input('region-dropdown', 'value'),
    Input('year-dropdown', 'value')
)
def update_page_1(region, year):
    return page3(region, year)