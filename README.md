# 🏃‍♀️🎧 Running BPM Recommender

This is a hybrid music recommendation system designed to match songs to your running tempo.  
It uses a combination of **audio features** (e.g., tempo, energy, danceability) and **tags/genres** to suggest your next track — no more skipping songs during your run!

---

## 🔍 Features

- 🎵 Hybrid recommendation: Combines tempo-based similarity and genre overlap.
- 🔄 Interactive terminal: Search and select your favorite song to get recommendations.
- 🧠 Euclidean and Jaccard-based similarity for better musical context.
- 🔥 Prevents recommending songs from the same artist back-to-back.
- 📂 Uses a static (for now) dataset (~1M Spotify tracks) for recommendations.
- ⚡️ Fast similarity computations using vectorized operations.

---

## 📁 Dataset

Due to GitHub’s file size limits, the dataset is stored externally:

👉 **[Download `tracks.csv` from Google Drive](https://drive.google.com/file/d/1pkDxIiFvYvomqT9YkTrjCwCA6HStJBSR/view?usp=sharing)**  
Place the file in the root folder of this project before running the app.

---

## 🚀 How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/marpapadopoulou/spotify_bpm_recsys.git
   cd spotify_bpm_recsys

2. **Install dependencies**

   pip install -r requirements.txt

3. **Run the recommender**

   python main.py
