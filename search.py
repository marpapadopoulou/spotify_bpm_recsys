import pandas as pd
from data_loader import load_data  
from rapidfuzz import fuzz

def search_song(df, title_query, artist_query=None, threshold=70):
    """
    Perform a fuzzy search for songs matching the title and (optional) artist.
    Returns a DataFrame with matches and similarity scores.
    """
    matches = []

    for idx, row in df.iterrows():
        title_score = fuzz.partial_ratio(title_query.lower(), row['name'].lower())
        artist_score = fuzz.partial_ratio(artist_query.lower(), row['artist'].lower()) if artist_query else 100
        
        # Combine title and artist match scores
        combined_score = (title_score + artist_score) / 2

        if combined_score >= threshold:
            matches.append((idx, combined_score))

    # Sort by score and return the matching rows
    matched_indices = [idx for idx, score in sorted(matches, key=lambda x: x[1], reverse=True)]
    return df.loc[matched_indices]


    



