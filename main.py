from recommender import combine_similarity, recommend_next_song
from data_loader import load_data
from search import search_song
import pandas as pd
import numpy as np
import random


# Load the dataset
all_songs = load_data('tracks.csv')

#ask the user for the song name and artist name
song_name = input("Enter the song name: ")
artist_name = input("Enter the artist name (optional): ")

#search for the song in the dataset
search_results = search_song(all_songs, song_name, artist_name)

#let the user select the song from the search results
if search_results .empty:
    print("No songs found. Search again.")
else:
    for i, row in search_results.iterrows():
        print(f"{i}: {row['name']} by {row['artist']}")
    selected_index = int(input("Select the song index: "))
    selected_song = search_results.loc[selected_index]


# Select a random song
#selected_song = all_songs.sample(1).iloc[0]

#remove the song from the all songs
#all_songs=all_songs[all_songs['track_id']!=selected_song['track_id']]

# Define the features to use in the recommendation
features = ['danceability', 'energy', 'tempo_scaled']

# Define the weight to assign to tags similarity
tags_weight = 0.5

# Recommend the next song
recommended_song = recommend_next_song(selected_song, all_songs, features, tags_weight)

print("\n Your next recommended song is:")
print(f"▶️ {recommended_song['name']} by {recommended_song['artist']}")





