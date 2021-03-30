"""
Functions for data wrangling, creating the model, and returning song
recommendations.
"""
import pandas as pd
from sklearn.neighbors import NearestNeighbors


# Data Wrangle function:
def wrangle(filepath):
    """
    Takes in filepath for the Spotify data.csv file.
    Returns a clean dataframe of song features to fit model.
    """
    df = pd.read_csv(filepath, parse_dates=['release_date'])

    # dropping name, artist column
    df = df.drop(['name', 'artists'], axis=1)
    # set ID as the index
    df.set_index('id', inplace=True)

    # rearranging similar features to be together to improve readability
    df = df[['valence', 'acousticness', 'danceability',
             'energy', 'instrumentalness', 'liveness', 'loudness',
             'speechiness', 'tempo'
             ]]
    # fixing loudness and tempo
    df['loudness'] = df.loudness.apply(lambda x: x / -100)
    df['tempo'] = df.tempo.apply(lambda x: x / 1000)
    df = df[df.loudness > 0.0]
    return df


def the_key(filepath):
    """
    Takes in filepath for the Spotify data.csv file.
    Returns a one-column dataframe that combines song track and artist and
    retains id as index.
    """
    df = pd.read_csv(filepath, parse_dates=['release_date'])
    # stripping artist column of:  [   ]  '  and  "
    df['artists'] = df['artists'].str.strip("[]")
    df['artists'] = df['artists'].str.strip("'")
    df['artists'] = df['artists'].str.strip('"')
    df['artists'] = df['artists'].str.lower()
    df['name'] = df['name'].str.lower()
    # set id as the index
    df.set_index('id', inplace=True)
    # combined song name and artist
    df['name_artist'] = df['name'] + ' - ' + df['artists']

    key = df['name_artist']
    return key


def create_fit_model(features_df):
    """
    Takes in a dataframe of song features and fits a KNN model.
    Returns the fitted model as knn_spotify.
    """
    model = NearestNeighbors(n_neighbors=10,
                             n_jobs=-1)
    knn_spotify = model.fit(features_df)
    return knn_spotify


# made changes here (filipe)
# set the function to only ask for user input, and we can give instructions
# on the webpage for the user to put in the name of the song and artist,
# or any part of either.
def recommended_songs(user_input, features_df, knn_spotify, filepath):
    """
    Takes in a user_input (song/artist).

    Returns the 'name_artist' column from recom_songs dataframe.
    """
    # making user input lower to not worry about capitalizations
    user_input = user_input.lower()
    key = the_key(filepath)
    # find what name_artist combo contains the user_input:
    selected_song = key.loc[key.str.contains(user_input)]
    # search the key df and return the song id
    song_id = selected_song.index.tolist()
    # feed the song id into the model
    song_row = features_df.loc[song_id, :]
    # model finds the NN and gives you back song id
    neigh_dist, neigh_index = knn_spotify.kneighbors(song_row)
    # random nn
    index = neigh_index.flat[0:10].tolist()
    # song_index = random.choice(index)
    # converting list to df for easier access
    recom_songs = key.iloc[index].to_frame()
    # list of songs with no ID and formatted as title
    recom_songs_list = recom_songs['name_artist'].to_list()
    for i in range(len(recom_songs_list)):
        recom_songs_list[i] = recom_songs_list[i].title()
    return recom_songs_list
