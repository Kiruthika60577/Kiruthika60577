import streamlit as st
import pandas as pd

# Title of your Streamlit app
st.title("WBSFlix - Movie Recommendations")

# Header
st.header("Movie Recommendations")

# Description
st.text("Enjoy personalized movie recommendations!")

# Input for User's Preferred Genre
genre = st.text_input("Enter your preferred movie genre")

# Load movies.csv from GitHub
movies_url = 'https://raw.githubusercontent.com/Kiruthika60577/Kiruthika60577/main/movies.csv'
movies_df = pd.read_csv(movies_url)

# Load ratings.csv from GitHub
ratings_url = 'https://raw.githubusercontent.com/Kiruthika60577/Kiruthika60577/main/ratings.csv'
ratings_df = pd.read_csv(ratings_url)

# Merge movies_df and ratings_df based on 'MovieId'
merged_df = movies_df.merge(ratings_df, on='MovieId', how='inner')

# Display recommended movies based on genre
if genre:
    genre = genre.lower()
    recommended_movies = merged_df[merged_df['genres'].str.lower().str.contains(genre)]
    
    if not recommended_movies.empty:
        st.subheader(f"Recommended {genre.capitalize()} Movies with Ratings")
        st.write(recommended_movies)
    else:
        st.warning(f"No {genre.capitalize()} movies found. Try a different genre.")
