"""THIS IS THE PAGE THAT WILL INITIALIZE OUR APP IN HEROKU, AND DO OTHER COOL
STUFF TOO IN A FEW DAYS OR SO
"""
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# models import function


# LETS GO

# def create_app():
#     """
#     Function to deploy heroku application.
#     Contains assortment of functions which control the inputs and outputs
#     of interactive web application.
#     """
app = Flask(__name__)
# load_model = load('finalized_model.sav')
# return app

@app.route('/')
def root():
    """
    Welcomes user.
    Gives information on what the app does.
    Button to 'Get Started' will take user to /song_selection.
    """
    return render_template('home.html')

@app.route('/about')
def about():
    """About the app and creators"""
    return "This is what it's all about!"

@app.route('/song_selection', methods=["POST"])
def song_selection():
    """
    Inputs user's song of choice.
    Moves user to recommendations page.
    """
    # Call model predict on song
    song_title = request.values['song_title']
    return render_template('song.html',
                           song_title=song_title)


@app.route('/recommendations')
def recommendations():
    """
    Returns song recommendations based on user's song of choice
    """
    return render_template('recommendations.html')
