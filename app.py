"""THIS IS THE PAGE THAT WILL INITIALIZE OUR APP IN HEROKU, AND DO OTHER COOL
STUFF TOO IN A FEW DAYS OR SO
"""
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


# LETS GO

# def create_app():
#     """
#     Function to deploy heroku application.
#     Contains assortment of functions which control the inputs and outputs
#     of interactive web application.
#     """
app = Flask(__name__)
# load_model = load('finalized_model.sav')

@app.route('/')
def root():
    """Home page"""
    return render_template('home.html')

@app.route('/about')
def about():
    """About the app and creators"""
    return "This is what it's all about!"

@app.route('/song_selection')
def song_selection():
    """Retrieves song selection"""
    return "Enter a song:"

@app.route('/recommendations')
def recommendations():
    """Returns song recommendations"""
    return "Here are some more songs just like it!"
