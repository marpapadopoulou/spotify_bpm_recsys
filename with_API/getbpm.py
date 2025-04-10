import requests
import time
from fetch_tracks import get_saved_tracks
from spotify_auth import sp

# Your API Key from GetSongBPM
API_KEY = "a11871b9a62f13d81ab8537607d2474d"

def search_song(title, artist):
    url = "https://api.getsong.co/search/"
    params = {
        "type": "both",
        "lookup": f"song:{title} artist:{artist}",
        "api_key": API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"❌ API error for '{title}' by '{artist}' - Status: {response.status_code}")
        return None

    try:
        data = response.json()
    except ValueError:
        print(f"❌ Failed to parse JSON for '{title}' by '{artist}'")
        return None

    # Debug output to inspect structure
    if not isinstance(data, dict) or "search" not in data:
        print(f"❌ Unexpected API structure for: {title} by {artist}")
        print("Response:", data)
        return None

    search_results = data["search"]
    
    if isinstance(search_results, list) and len(search_results) > 0:
        return search_results[0]
    else:
        print(f"❌ No results for: {title} by {artist}")
        print("Raw search response:", search_results)
        return None

def get_song_details(song_id):
    url = "https://api.getsong.co/song/"
    params = {
        "id": song_id,
        "api_key": API_KEY
    }

    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print(f"❌ Failed to fetch details for song ID: {song_id}")
        return None

    return response.json().get("song")

# Step 1: Get your saved tracks from Spotify
saved_tracks = get_saved_tracks(sp, limit=50)

# Step 2: For each track, search for it in GetSongBPM and fetch audio details
for track in saved_tracks:
    title = track["name"]
    artist = track["artist"]

    song = search_song(title, artist)

    if song:
        details = get_song_details(song["id"])
        if details:
            bpm = details.get("tempo")
            danceability = details.get("danceability")
            print(f"✅ {title} by {artist} - BPM: {bpm}, Danceability: {danceability}")
        else:
            print(f"⚠️ Could not get full details for {title} by {artist}")
    else:
        print(f"❌ Not found on GetSongBPM: {title} by {artist}")

    time.sleep(0.5)  # To avoid hitting rate limits (3000/hour = ~0.8/sec)
