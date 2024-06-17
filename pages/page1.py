from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from data import df

# Функции для создания графиков


def create_migration_vs_income_graph(filtered_df):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=filtered_df['municipality'], y=filtered_df['migration'], name = 'Миграция'))
    #fig.add_trace(go.Bar(x=filtered_df['municipality'], y=filtered_df['income'], name = 'Доход'))
    fig.update_layout(title_text='Миграционный прирост района')
    return fig

def create_payment_over_years_graph(filtered_df):
    grouped_df = filtered_df.groupby('year')['payment'].sum().reset_index()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=grouped_df['year'], y=grouped_df['payment'], mode='lines'))
    fig.update_layout(title_text='Динамика фонда заработной платы региона')
    return fig

def create_income_vs_payment_graph(filtered_df):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=filtered_df['municipality'], y=filtered_df['income'], name='Доходы'))
    fig.add_trace(go.Bar(x=filtered_df['municipality'], y=filtered_df['payment'], name='Выплаты'))
    fig.update_layout(title_text='Доход района и сумма социальных выплат', barmode='group')
    return fig

# Основная функция для создания разметки с графиками
def create_page_1_layout(region, year):
    filtered_df = df[(df['region'] == region) & (df['year'] == year)]

    layout = html.Div([
        dbc.Row([
            dbc.Col(dcc.Graph(figure=create_migration_vs_income_graph(filtered_df)), width=5, style={'border': 'solid 2px', 'border-radius': '20px', 'margin': '15px'}),
            dbc.Col(dcc.Graph(figure=create_payment_over_years_graph(df[(df['region'] == region)])), width=5, style={'border': 'solid 2px', 'border-radius': '20px', 'margin': '15px'}),
        ]),
        dbc.Row([
            
            dbc.Col(dcc.Graph(figure=create_income_vs_payment_graph(filtered_df)), width=5, style={'border': 'solid 2px', 'border-radius': '20px', 'margin': '15px', 'width': '120vh'})
        ])
    ], style={'margin': '20px'})
    return layout

layout = dbc.Container([
    dbc.Row([
        dcc.Dropdown(
            options=[{'label': region, 'value': region} for region in df['region'].unique()],
            value=df['region'].unique()[0],
            id='region-dropdown'
        ),
        dcc.Dropdown(
            options=[{'label': year, 'value': year} for year in df['year'].unique()],
            value=df['year'].unique()[0],
            id='year-dropdown'
        )
    ]),
    dbc.Row([
        html.Div(id='page-1-graph-container')
    ])
])

@callback(
    Output('page-1-graph-container', 'children'),
    Input('region-dropdown', 'value'),
    Input('year-dropdown', 'value')
)
def update_page_1(region, year):
    return create_page_1_layout(region, year)
