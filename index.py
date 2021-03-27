# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
#from PIL import Image
# Imports from this application
from app import create_app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Song suggestion app based on a users song input

            This app will allow users to examine the audio features of over 160k songs collected from Spotify.

            """
        ),
        dcc.Link(dbc.Button('Predict!', color='primary'), href='/predictions')
    ],
    md=4,
)

# gapminder = px.data.gapminder()
# im1 = Image.open(r"C:\Users\Gigabyte\Desktop\Misc papers\School\Lambda\Data Science\Unit 3\Unit3\week\assets\spotify-playlists-getty-mahmut-serdar-alakus")
# im1 = im1.save("Spotify.jpg")

 column2 = dbc.Col(
     [
         html.Img(src='assets/imagefile.extension', className='img-fluid')
     ]
 )

 layout = dbc.Row([column1, column2])