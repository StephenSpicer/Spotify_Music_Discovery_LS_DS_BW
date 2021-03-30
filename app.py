"""THIS IS THE PAGE THAT WILL INITIALIZE OUR APP IN HEROKU, AND DO OTHER COOL
STUFF TOO IN A FEW DAYS OR SO
"""
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from functions import wrangle, the_key, create_fit_model, recommended_songs
# functions import function
# read in file, wrangle, key
# create model


# LETS GO

# def create_app():
#     """
#     Function to deploy heroku application.
#     Contains assortment of functions which control the inputs and outputs
#     of interactive web application.
#     """
app = Flask(__name__)

# create song features dataframe for model
features_df = wrangle("./data/data.csv")
# create key dataframe of id and song_artist
key = the_key("./data/data.csv")
# instantiate model
knn_spotify = create_fit_model(features_df)


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
    song_title = request.values['song_title']
    suggestions = recommended_songs(str(song_title),
                                    features_df,
                                    knn_spotify,
                                    "./data/data.csv")
    print(type(suggestions))
    return render_template('recommendations.html',
                           song_title=song_title,
                           suggestions=suggestions)
