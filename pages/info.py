from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col(
                html.Div([
                html.H3("Информация о проекте"),
                html.Hr(style={'color': 'black', 'border':'solid 1px'}),
            ], style={'textAlign': 'center'})
        )
    ]),
    dbc.Row([
        #html.Div(id='page-5-graph-container')
        html.P("Цель проекта - визуализация статистических данных, таких как:"),
        html.Div([
            html.P("-миграционный прирост муниципальных районов РФ;"),
            html.P("-динамика фонда заработной платы регионов РФ;"),
            html.P("-доход и сумма социальных выплат муниципальных районов РФ;"),
            html.P("-состав дохода региона РФ от муниципальных районов РФ;"),
            html.P("-численность населения муниципальных районов РФ;"),
            html.P("-доход региона РФ;"),
            html.P("-миграционный прирост муниципальных районов РФ."),
        ], style = {'padding-left': '3rem'}),   
        html.P("Все эти данные будут полезны исследователям, политическим деятелям, а также некоторые данные будут полезны людям, которые планируют переехать в другой регион."),
        html.Br(),
        html.P("Проект представлен в виде дашборда с разными диаграммами, которые отображают информацию по определенным показателям."),
        html.A("Ссылка на GitHub проекта", href = 'https://github.com/ZhigalovArtem/Dashboard', style = {'text-align':'center', 'color':'darkblue'}),
    ], style ={'font-size':'18px', 'background': '#B29D8D', 'border-radius':'10px', 'padding':'1rem 0.5rem 0.5rem 1rem'})
], style = {'margin-bottom': '19.95rem'})