import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from dotenv import load_dotenv


#load the environment variables
load_dotenv()

#retrieve client credentials
#client_id =os.getenv('SPOTIFY_CLIENT_ID')
#client_secret =os.getenv('SPOTIFY_CLIENT_SECRET') 

print("Client ID from env:", os.getenv("SPOTIFY_CLIENT_ID"))


# Explicitly set the environment variables that Spotipy expects
os.environ["SPOTIPY_CLIENT_ID"] = os.getenv("SPOTIFY_CLIENT_ID")
os.environ["SPOTIPY_CLIENT_SECRET"] = os.getenv("SPOTIFY_CLIENT_SECRET")
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8888/callback"


#define scope (what access i want)
scope = "user-library-read user-read-recently-played user-top-read user-read-playback-state user-modify-playback-state"

#authenticate the user
sp=spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

