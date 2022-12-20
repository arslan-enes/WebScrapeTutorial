import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

load_dotenv()
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=os.getenv("CLIENT_ID"),
                                                                              client_secret=os.getenv("CLIENT_SECRET"),
                                                                              ),
                          requests_timeout=None)


def search_artist_song(artist, song):
    results = spotify.search(q=f'artist:{artist} track:{song}', type='track')
    items = results['tracks']['items']
    if len(items) > 0:
        print(f"{artist}-{song}")
        print(spotify.audio_features(items[0]['id']))
        print("*"*24)
        return spotify.audio_features(items[0]['id'])
    else:
        return None


if __name__ == '__main__':
    search_artist_song('the cure', 'friday im in love')