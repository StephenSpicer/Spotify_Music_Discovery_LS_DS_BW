"""
Functions for data wrangling, creating the model, and returning song
recommendations.
"""


# Data Wrangle function:
def wrangle(filepath):
    df = pd.read_csv(filepath, parse_dates=['release_date'])

    # dropping name, artist column
    df = df.drop(['name', 'artists'], axis=1)
    # set ID as the index
    df.set_index('id', inplace=True)

    # rearraging similar features to be together to improve readability
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
    model = NearestNeighbors(n_neighbors=10,
                             n_jobs=-1)
    knn_spotify = model.fit(x)
    return knn_spotify


def recommended_songs(user_input):
    key = the_key(data_path)
    # find what name_artist combo contains the user_input:
    selected_song = key.loc[key.str.contains(user_input)]
    # search the key df and return the song id
    song_id = selected_song.index.tolist()
    # feed the song id into the model
    song_row = x.loc[song_id, :]
    # model finds the NN and gives you back song id
    neigh_dist, neigh_index = knn_spotify.kneighbors(song_row)
    index = neigh_index.flat[0:10].tolist()
    # song_index = random.choice(index)
    # convert the index of the suggested song to the song_id
    # This code is returning the column headers, not the index atm
    # not sure how this code works, will talk to Nick.
    # song_suggest = key.iloc[song_index].to_frame().columns.item()
    # converting list to df for easier access
    recom_songs = key.iloc[index].to_frame()

    # return the song id to plug into the spotify appi and have song play
    return recom_songs['name_artist']
