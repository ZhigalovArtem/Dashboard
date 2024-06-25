from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from data import df

def create_budget_pie_chart(filtered_df):
    fig = go.Figure()
    fig.add_trace(go.Pie(labels=filtered_df['municipality'], values=filtered_df['income']))
    fig.update_layout(title_text='Состав дохода региона', paper_bgcolor='#AF947F', plot_bgcolor='#AF947F')
    return fig

def pie_chart_layout(region, year):
    filtered_df = df[(df['region'] == region) & (df['year'] == year)]
    layout = html.Div([
        dbc.Row([
            dbc.Col(dcc.Graph(figure=create_budget_pie_chart(filtered_df)), width=15, style={'border': 'solid 2px', 'border-radius': '20px'})
        ])
    ], style={'margin': '15px', 'padding-top': '10%', 'margin-bottom': '13.6rem'})
    return layout


layout = dbc.Container([
    dbc.Row([
        dcc.Dropdown(
            options=[{'label': region, 'value': region} for region in df['region'].unique()],
            value=df['region'].unique()[0],
            id='region-dropdown',
            style={'margin-bottom':'2px'}
        ),
        dcc.Dropdown(
            options=[{'label': year, 'value': year} for year in df['year'].sort_values().unique()],
            value=df['year'].unique()[0],
            id='year-dropdown'
        )
    ]),
    dbc.Row([
        html.Div(id='page-2-graph-container')
    ])
])



@callback(
    Output('page-2-graph-container', 'children'),
    Input('region-dropdown', 'value'),
    Input('year-dropdown', 'value')
)
def update_page_1(region, year):
    return pie_chart_layout(region, year)