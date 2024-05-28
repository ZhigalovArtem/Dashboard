import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Загрузка данных из файла
file_path = '1.xlsx'
df = pd.read_excel(file_path)

app = Dash(__name__)

# Создание элементов дашборда
app.layout = html.Div([
    html.H1("Двухстраничный Дашборд"),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Страница 1', value='tab-1'),
        dcc.Tab(label='Страница 2', value='tab-2'),
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.Div([
                dcc.Dropdown(
                    id='region-dropdown',
                    options=[{'label': region, 'value': region} for region in df['region'].unique()],
                    value=df['region'].unique()[0],
                    style={'width': '48%', 'display': 'inline-block'}
                ),
                dcc.Dropdown(
                    id='year-dropdown',
                    options=[{'label': year, 'value': year} for year in df['year'].unique()],
                    value=df['year'].unique()[0],
                    style={'width': '48%', 'display': 'inline-block'}
                )
            ], style={'padding': '10px'}),
            dcc.Graph(id='page-1-graph')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.Div([
                dcc.Dropdown(
                    id='region-dropdown-2',
                    options=[{'label': region, 'value': region} for region in df['region'].unique()],
                    value=df['region'].unique()[0],
                    style={'width': '48%', 'display': 'inline-block'}
                ),
                dcc.Dropdown(
                    id='year-dropdown-2',
                    options=[{'label': year, 'value': year} for year in df['year'].unique()],
                    value=df['year'].unique()[0],
                    style={'width': '48%', 'display': 'inline-block'}
                )
            ], style={'padding': '10px'}),
            dcc.Graph(id='page-2-graph')
        ])

@app.callback(
    Output('page-1-graph', 'figure'),
    Input('region-dropdown', 'value'),
    Input('year-dropdown', 'value'))
def update_page_1(region, year):
    filtered_df = df[(df['region'] == region) & (df['year'] == year)]
    
    fig = make_subplots(rows=3, cols=2, subplot_titles=[
        'Численность населения региона в зависимости от фонда зарплаты',
        'Миграционный прирост региона в зависимости от фонда зарплаты',
        'Из чего состоит бюджет РФ сумма доходов региона',
        'Сумма дохода одного региона за несколько лет',
        'Динамика фонда заработной платы в зависимости от одного региона',
        'Сумма доходов региона и сумма социальных выплат'
    ], specs=[
        [{'type': 'xy'}, {'type': 'xy'}],
        [{'type': 'domain'}, {'type': 'xy'}],
        [{'type': 'xy'}, {'type': 'xy'}]
    ], vertical_spacing=0.3, horizontal_spacing=0.15)
    
    # Численность населения региона в зависимости от фонда зарплаты
    fig.add_trace(go.Bar(x=filtered_df['municipality'], y=filtered_df['income']), row=1, col=1)
    
    # Миграционный прирост региона в зависимости от фонда зарплаты
    fig.add_trace(go.Scatter(x=filtered_df['municipality'], y=filtered_df['migration'], mode='lines'), row=1, col=2)
    fig.add_trace(go.Bar(x=filtered_df['municipality'], y=filtered_df['income']), row=1, col=2)
    
    # Из чего состоит бюджет РФ сумма доходов региона
    fig.add_trace(go.Pie(labels=filtered_df['municipality'], values=filtered_df['income'],
                         domain=dict(x=[0, 1], y=[0, 1])), row=2, col=1)
    
    # Сумма дохода одного региона за несколько лет
    fig.add_trace(go.Scatter(x=filtered_df['year'], y=filtered_df['income'], mode='lines'), row=2, col=2)
    
    # Динамика фонда заработной платы в зависимости от одного региона
    fig.add_trace(go.Scatter(x=filtered_df['year'], y=filtered_df['payment'], mode='lines'), row=3, col=1)
    
    # Сумма доходов региона и сумма социальных выплат
    fig.add_trace(go.Bar(x=filtered_df['municipality'], y=filtered_df['income']), row=3, col=2)
    fig.add_trace(go.Bar(x=filtered_df['municipality'], y=filtered_df['payment']), row=3, col=2)
    
    fig.update_layout(height=1200, width=1500, title_text="Дашборд - Страница 1", margin=dict(t=50, b=50, l=50, r=50))
    return fig

@app.callback(
    Output('page-2-graph', 'figure'),
    Input('region-dropdown-2', 'value'),
    Input('year-dropdown-2', 'value'))
def update_page_2(region, year):
    filtered_df = df[(df['region'] == region) & (df['year'] == year)]
    
    fig = make_subplots(rows=1, cols=2, subplot_titles=[
        'Тепловая карта с приростом населений',
        'Тепловая карта с привлекательности региона для миграции'
    ], specs=[
        [{'type': 'heatmap'}, {'type': 'heatmap'}]
    ])
    
    # Тепловая карта с приростом населений
    fig.add_trace(go.Heatmap(
        z=filtered_df['population_growth'],
        x=filtered_df['municipality'],
        y=filtered_df['year']
    ), row=1, col=1)
    
    # Тепловая карта с привлекательности региона для миграции
    fig.add_trace(go.Heatmap(
        z=filtered_df['migration'],
        x=filtered_df['municipality'],
        y=filtered_df['year']
    ), row=1, col=2)
    
    fig.update_layout(height=600, width=1500, title_text="Дашборд - Страница 2", margin=dict(t=50, b=50, l=50, r=50))
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
