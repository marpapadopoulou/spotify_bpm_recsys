from spotify_auth import sp
import pandas as pd


#fetch all saved tracks 
def get_saved_tracks(sp, limit=50):
    saved_tracks = []
    offset = 0

    while True:
        results = sp.current_user_saved_tracks(limit=limit, offset=offset)
        if not results['items']:
            break

        for item in results['items']:
            track = item['track']
            saved_tracks.append({
                "name": track['name'],
                "artist": track['artists'][0]['name'],
                "id": track['id']
            })

        offset += limit

    return saved_tracks

# Fetch and print
saved = get_saved_tracks(sp)
#print(f"Fetched {len(saved)} saved tracks 🎉")

# Preview a few tracks
#for i, t in enumerate(saved[:10]):
#    print(f"{i+1}. {t['name']} by {t['artist']} | ID: {t['id']}")

