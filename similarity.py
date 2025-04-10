import numpy as np
import pandas as pd

def jaccard_similarity(list1, list2):
    #convert lists to sets to calculate intersection and union
    list1=set(list1)
    list2=set(list2)
    intersection = len(list1 & list2)
    union = len(list1 | list2)
    return float(intersection) / union if union != 0 else 0 #avoid division by zero

def compute_similarity(selected_song, all_songs, features):
    """
    Compute similarity (1 / (1 + Euclidean distance)) for all songs.
    
    Parameters:
    - selected_song: Pandas Series (selected song)
    - all_songs: Pandas DataFrame (other songs in the dataset)
    - features: List of feature names to use in the calculation
    
    Returns:
    - DataFrame with track_id, name, and similarity score
    """
    # Create a copy to avoid modifying a slice
    all_songs = all_songs.copy()
    
    #convert to numpy arrays for faster computation
    
    selected_features = np.array(selected_song[features],  dtype=np.float64).reshape(1, -1)
    all_features = np.array(all_songs[features], dtype=np.float64)
    
    distances=np.linalg.norm(all_features-selected_features, axis=1)
    
    all_songs['similarity_features'] = 1 / (1 + distances)
    
    #return the similarity score as series not a dataframe
    return pd.Series(data=all_songs['similarity_features'].values, index=all_songs.index)