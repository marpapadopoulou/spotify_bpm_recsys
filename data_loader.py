import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def load_data(file_path):
    #load data from csv file 
    tracks=pd.read_csv(file_path)

    #keep selected columns
    selected_features=['track_id', 'name', 'artist','tags', 'danceability', 'energy', 'tempo']
    df_selected=tracks[selected_features]

    #handle missing values
    missing_values=df_selected.isnull().sum()
    #print(missing_values)

    #drop rows with missing values
    df_selected=df_selected.dropna()

    #check for duplicates
    duplicates=df_selected.duplicated().sum()

    #drop tempo values < 0 because it is not possible to have negative tempo
    df_selected=df_selected[df_selected['tempo']>0]

    #convert tags to list 
    df_selected['tags']=df_selected['tags'].apply(lambda x: x.split(", ") if isinstance(x, str) else [])

    scaler=MinMaxScaler()

    #normalize tempo 
    df_selected['tempo_scaled']=scaler.fit_transform(df_selected[['tempo']])
    
    return df_selected