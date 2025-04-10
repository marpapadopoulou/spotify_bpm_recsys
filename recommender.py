import pandas as pd
import numpy as np
from similarity import jaccard_similarity, compute_similarity

#combine similarity scores from tags and features

def combine_similarity(selected_song, all_songs, features, tags_weight):
    """
    Combine similarity scores from tags and features.
    
    Parameters:
    - selected_song: Pandas Series (selected song)
    - all_songs: Pandas DataFrame (other songs in the dataset)
    - features: List of feature names to use in the calculation
    - tags_weight: Weight to assign to tags similarity
    
    Returns:
    - DataFrame with track_id, name, and combined similarity score
    """
    
    all_songs = all_songs.copy()
    
    # Compute similarity based on features
    all_songs["similarity_features"] = compute_similarity(selected_song, all_songs, features)
    
    # Compute similarity based on tags
    all_songs["similarity_tags"] = all_songs['tags'].apply(lambda tags: jaccard_similarity(selected_song['tags'], tags))
    
    # Combine similarity scores
    all_songs['final_similarity'] = (1 - tags_weight) * all_songs['similarity_features'] + tags_weight * all_songs['similarity_tags']
    
    return all_songs.sort_values(by='final_similarity', ascending=False)

def recommend_next_song(selected_song, all_songs, features, tags_weight):
    """
    Recommend the next song based on the selected song.
    
    Parameters:
    - selected_song: Pandas Series (selected song)
    - all_songs: Pandas DataFrame (other songs in the dataset)
    - features: List of feature names to use in the calculation
    - tags_weight: Weight to assign to tags similarity
    
    Returns:
    - Pandas Series with the recommended song
    """
    
    # Compute combined similarity
    similar_songs = combine_similarity(selected_song, all_songs, features, tags_weight)
    
    #remove the song from the same artist as the selected song
    filtered_songs = similar_songs[similar_songs['artist'] != selected_song['artist']]
    
    #if diverse song exists, select the top one
    if not filtered_songs.empty:
        return filtered_songs.iloc[0]
        
    #if no diverse song exists, select the top song
    return similar_songs.iloc[0] if not similar_songs.empty else None