import pandas as pd
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

# Загрузка данных из файла
file_path = '1.xlsx'
df = pd.read_excel(file_path)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Функция для создания отдельных графиков
def create_population_vs_income_graph(filtered_df):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=filtered_df['municipality'], y=filtered_df['income']))
    fig.update_layout(title_text='Численность населения региона в зависимости от фонда зарплаты')
    return fig

def create_migration_vs_income_graph(filtered_df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_df['municipality'], y=filtered_df['migration'], mode='lines'))
    fig.add_trace(go.Bar(x=filtered_df['municipality'], y=filtered_df['income']))
    fig.update_layout(title_text='Миграционный прирост региона в зависимости от фонда зарплаты')
    return fig

def create_budget_pie_chart(filtered_df):
    fig = go.Figure()
    fig.add_trace(go.Pie(labels=filtered_df['municipality'], values=filtered_df['income']))
    fig.update_layout(title_text='Из чего состоит бюджет РФ сумма доходов региона')
    return fig

def create_income_over_years_graph(filtered_df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_df['year'], y=filtered_df['income'], mode='lines'))
    fig.update_layout(title_text='Сумма дохода одного региона за несколько лет')
    return fig

def create_payment_over_years_graph(filtered_df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_df['year'], y=filtered_df['payment'], mode='lines'))
    fig.update_layout(title_text='Динамика фонда заработной платы в зависимости от одного региона')
    return fig

def create_income_vs_payment_graph(filtered_df):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=filtered_df['municipality'], y=filtered_df['income'], name='Income'))
    fig.add_trace(go.Bar(x=filtered_df['municipality'], y=filtered_df['payment'], name='Payment'))
    fig.update_layout(title_text='Сумма доходов региона и сумма социальных выплат', barmode='group')
    return fig

# Основная функция для создания разметки с графиками
def create_page_1_layout(region, year):
    filtered_df = df[(df['region'] == region) & (df['year'] == year)]

    layout = html.Div([
        dbc.Row([
            dbc.Col(dcc.Graph(figure=create_population_vs_income_graph(filtered_df)), width=6),
            dbc.Col(dcc.Graph(figure=create_migration_vs_income_graph(filtered_df)), width=6)
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(figure=create_budget_pie_chart(filtered_df)), width=6),
            dbc.Col(dcc.Graph(figure=create_income_over_years_graph(filtered_df)), width=6)
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(figure=create_payment_over_years_graph(filtered_df)), width=6),
            dbc.Col(dcc.Graph(figure=create_income_vs_payment_graph(filtered_df)), width=6)
        ])
    ])
    return layout

# Создание элементов дашборда
app.layout = html.Div([
    html.H1("Двухстраничный Дашборд"),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Страница 1', value='tab-1', children=[
            html.Div([
                dcc.Dropdown(
                    id='region-dropdown',
                    options=[{'label': region, 'value': region} for region in df['region'].unique()],
                    value=df['region'].unique()[0]
                ),
                dcc.Dropdown(
                    id='year-dropdown',
                    options=[{'label': year, 'value': year} for year in df['year'].unique()],
                    value=df['year'].unique()[0]
                ),
                html.Div(id='page-1-graph-container')
            ])
        ]),
        dcc.Tab(label='Страница 2', value='tab-2', children=[
            html.Div([
                dcc.Dropdown(
                    id='region-dropdown-2',
                    options=[{'label': region, 'value': region} for region in df['region'].unique()],
                    value=df['region'].unique()[0]
                ),
                dcc.Dropdown(
                    id='year-dropdown-2',
                    options=[{'label': year, 'value': year} for year in df['year'].unique()],
                    value=df['year'].unique()[0]
                ),
                html.Div(id='page-2-graph-container')
            ])
        ]),
    ]),
])

@app.callback(
    Output('page-1-graph-container', 'children'),
    Input('region-dropdown', 'value'),
    Input('year-dropdown', 'value'))
def update_page_1(region, year):
    return create_page_1_layout(region, year)

@app.callback(
    Output('page-2-graph-container', 'children'),
    Input('region-dropdown-2', 'value'),
    Input('year-dropdown-2', 'value'))
def update_page_2(region, year):
    # Эта часть кода остается без изменений, аналогично page-1, вы можете создать отдельные функции для графиков страницы 2
    return html.Div([])  # Заглушка, доработайте аналогично page-1

if __name__ == '__main__':
    app.run_server(debug=True)
