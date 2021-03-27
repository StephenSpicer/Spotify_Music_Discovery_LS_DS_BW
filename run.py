# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import create_app
from pages import about, index, predictions
navbar = dbc.NavbarSimple(
    brand='Spotify Song Prediction',
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('About', href='/about', className='nav-link')), 
        dbc.NavItem(dcc.Link('Predictions', href='/predictions', className='nav-link')),
        dbc.NavItem(dcc.Link('Index', href='/index', className='nav-link'))
    ],
    sticky='top',
    color='primary', 
    light=False, 
    dark=True
)


footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                   html.Span('Lambda School Data Science Project', className='mr-2'), 
                   html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/Build-Week-Spotify-Song-Suggestion'), 
                ], 
                className='lead'
            )
        )
    )
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    navbar, 
    dbc.Container(id='page-content', className='mt-4'), 
    html.Hr(), 
    footer
])

if __name__ == '__main__':
    create_app.run_server(debug=True, threaded=True)
