# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd 
#from test import apidf

# Imports from this application
from app import create_app, track_id
#returns a random song from the kmeans model
ssuggest = suggestion
# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ##### Find the song ID of a song you enjoy listening to and paste it into the prediction generator to disvover new music.
            In order to find the song ID, open spotify and search for the song you would like to use. Click on "..." next to the song and navigate to the share tab. Copy the song link and paste it into a notes page.
            The result should look something like,
            https://open.spotify.com/track/5ervA7lbl13K2ekOUFmgKe
            The numbers and letters following /track/ are the song ID. Input this into the prediction generator to discover new music.

            """
        ),
    ],
    md=6,
)

column2 = dbc.Col(
    [
            html.Label('Song ID: '),
            dcc.Input(id = 'Track ID',
                      type = 'text',
                      placeholder='Track ID'),
            html.Br(), html.Br(),
            html.Button('Submit', id='btn-submit'),
            html.Label('Input your track ID: '),
            html.Div(id='output-submit'),
            html.Br(), html.Hr(),
            html.Div(f'Here is a song you may enjoy! {ssuggest}', style={'whiteSpace': 'pre-line'})
    ]
)


layout = dbc.Row([column1, column2])

html.Div(id='intermediate-value', style={'display': 'none'})





#Stuff I'm working on

# for store in ('session'):
#     @app.callback(Output(store, 'data'),
#                   Input('{}-button'.format(store), 'n_clicks'),
#                   State(store, 'data'))
#     def on_click(n_clicks, data):
#         if n_clicks is None:
#             raise PreventUpdate
#         data = data or {'clicks': 0}
#         data['clicks'] = data['clicks'] + 1
#         return data
#     @app.callback(Output('{}-clicks'.format(store), 'children'),
#                   Input(store, 'modified_timestamp'),
#                   State(store, 'data'))
#     def on_data(ts, data):
#         if ts is None:
#             raise PreventUpdate
#         data = data or {}
#         return data.get('clicks', 0)

# def handle_upload(track_id):
#     if track_id == None:
#         return pd.DataFrame({}).to_json()
#     e = pd.read_csv(io.StringIO(track_id))
#     return e.to_json()