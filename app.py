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


@app.route('/song_selection')
def song_selection():
    """
    Inputs user's song of choice.
    Moves user to recommendations page.
    """
    # Call model predict on song
    return render_template('song.html')



@app.route('/recommendations', methods=['POST'])
def recommendations():
    """
    Returns song recommendations based on user's song of choice
    """
    fake_suggestions = ["Song 1 - Artist 1", "Song 2 - Artist 2",
                        "Song 3 - Artist 3", "Song 4 - Artist 4"]
    song_title = request.values['song_title']
    return render_template('recommendations.html',
                           song_title=song_title,
                           suggestions=fake_suggestions)
