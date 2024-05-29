from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import data as df
from pages import page1, page2, page3

external_stylesheets = [dbc.themes.JOURNAL]  # Выберите тему из https://bootswatch.com/

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

# Задаем аргументы стиля для боковой панели
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#987156",
}

# Справа от боковой панели размещается основной дашборд
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# Создание боковой панели
sidebar = html.Div(
    [
        html.H2("Данные регионов России", className="display-6"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Страница 1", href="/page-1", active="exact"),
                dbc.NavLink("Круговая", href="/page-2", active="exact"),
                dbc.NavLink("Численность населения и доход региона", href="/page-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return page1.layout
    elif pathname == "/page-1":
        return page1.layout
    elif pathname == "/page-2":
        return page2.layout
    elif pathname == "/page-3":
        return page3.layout
    # Если пользователь попытается перейти на другую страницу, верните сообщение 404
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

if __name__ == '__main__':
    app.run_server(debug=True)
