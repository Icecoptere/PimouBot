import os
import sys
import json
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

from dotenv import load_dotenv
from spotipy import oauth2

load_dotenv()

# configure the Spotify API
scope = 'playlist-modify-public'
username = "Pimouki"
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = 'http://localhost:8888/callback'

# get the Spotify authentication token for the user

sp_oauth = oauth2.SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                               redirect_uri=redirect_uri, scope=scope, cache_path=".cache-" + username)

# get the user's authentication token or refresh it if expired
token_info = sp_oauth.get_cached_token()
if not token_info:
    auth_url = sp_oauth.get_authorize_url()
    print("Please visit this URL to authorize the application: " + auth_url)
    response = input("Enter the URL you were redirected to: ")
    code = sp_oauth.parse_response_code(response)
    token_info = sp_oauth.get_cached_token()
    if not token_info:
        token_info = sp_oauth.get_access_token(code)

# create a Spotify object using the token
sp = spotipy.Spotify(auth=token_info['access_token'])

# define the playlist ID for the target playlist
playlist_id = "4vbADzemxKl7b6kL8CClEd"


# define a function to add a track to the playlist
def add_track_to_playlist(track_uri):
    results = sp.user_playlist_add_tracks(username, playlist_id, [track_uri])
    return results
