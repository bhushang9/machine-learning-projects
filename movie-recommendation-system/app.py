#running app [python -m streamlit run app.py]

import streamlit as st
import pandas as pd
import requests
import pickle

# Load the processed movie data and cosine similarity matrix
with open('movie_data.pkl', 'rb') as file:
    movies, cosine_sim = pickle.load(file)

# Function to fetch movie poster from TMDB API
def fetch_poster(movie_id):
    api_key = '8e132593f9fb0a0e5f362801fa091121'  
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    
    # Fallback poster if not found
    return "https://via.placeholder.com/500x750?text=No+Image"

# Function to get top 10 similar movies
def get_recommendations(title, cosine_sim=cosine_sim):
    try:
        idx = movies[movies['title'] == title].index[0]
    except IndexError:
        return pd.DataFrame(columns=['title', 'movie_id'])

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Top 10 (excluding the selected movie itself)
    movie_indices = [i[0] for i in sim_scores]
    return movies[['title', 'movie_id']].iloc[movie_indices]

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬Movie Recommendation System")

selected_movie = st.selectbox("📽️ Choose a movie to get recommendations:", movies['title'].values)

if st.button('Recommend'):
    recommendations = get_recommendations(selected_movie)
    st.subheader("Top 10 Recommendations")

    # Display in 2x5 grid
    for i in range(0, 10, 5):
        cols = st.columns(5)
        for col, j in zip(cols, range(i, i+5)):
            if j < len(recommendations):
                movie_title = recommendations.iloc[j]['title']
                movie_id = recommendations.iloc[j]['movie_id']
                poster_url = fetch_poster(movie_id)
                with col:
                    st.image(poster_url, width=140)
                    st.caption(movie_title)
  