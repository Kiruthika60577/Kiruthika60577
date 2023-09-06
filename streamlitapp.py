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

# Load links.csv from GitHub
links_url = 'https://raw.githubusercontent.com/Kiruthika60577/Kiruthika60577/main/links.csv'
links_df = pd.read_csv(links_url)

# Load tags.csv from GitHub
tags_url = 'https://raw.githubusercontent.com/Kiruthika60577/Kiruthika60577/main/tags.csv'
tags_df = pd.read_csv(tags_url)

# Display recommended movies based on genre
if genre:
    genre = genre.lower()
    recommended_movies = movies_df[movies_df['Genre'].str.lower().str.contains(genre)]
    
    if not recommended_movies.empty:
        st.subheader(f"Recommended {genre.capitalize()} Movies")
        st.write(recommended_movies)
    else:
        st.warning(f"No {genre.capitalize()} movies found. Try a different genre.")
