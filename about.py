# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import create_app #I don't think this is necessary

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
             ## About
            This app was constructed in order to help users find new music they might enjoy.
            
            It is constructed with songs between year 1921 and 2020 and contains over 160,000 songs from various artists.
            Visit the Predictions page in order to discover new music!
            Constructed by Marcos Morales, Nick Major, and William Leibundgut



            """
        ),

    ],
)

layout = dbc.Row([column1])