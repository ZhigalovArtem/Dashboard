from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px

from data import df, counties

grouped_df = df.groupby(['cartodb_id', 'region'])['migration'].sum().reset_index()

rusmap = px.choropleth_mapbox(
                        grouped_df,
                        geojson=counties,
                        featureidkey='properties.cartodb_id',
                        color='migration', #решить какой показатель
                        locations='cartodb_id',
                        color_continuous_scale=[
                      [0, 'rgb(240,240,240)'],
                      [0.005, 'rgb(227,26,28,0.5)'],
                      [0.7, 'rgb(180,228,25)'],
                      [1, 'rgb(0,204,0)']],
                        range_color=(-2300000,1500000),
                        mapbox_style="carto-positron",
                        zoom=20,
                        opacity=0.5,
                        hover_name = 'region',
                        hover_data = {'region':True, 'cartodb_id':False},
                        labels={'region':'Субъект РФ'}
)
rusmap.update_layout(mapbox_style="carto-positron",
                        margin={"r":0,"t":0,"l":0,"b":0}, geo_scope='asia',
                        mapbox_zoom=1, mapbox_center = {"lat": 66, "lon": 94}, height=500,
                        showlegend=False)

layout = dbc.Container([
    dbc.Row ([
        dbc.Col(
                html.Div([
                html.H3("Миграция в регионах РФ"),
                html.Hr(style={'color': 'black', 'border':'solid 1px'}),
            ], style={'textAlign': 'center'})
        )
    ]),


    html.Br(),


    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=rusmap)
            ],width=12, style={'border': 'solid 2px', 'border-radius': '20px', 'padding':'15px', 'margin-bottom': '16.8rem'}),
    ]),
])
