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

# Check column names in both DataFrames
st.write("Movies DataFrame Columns:", movies_df.columns)
st.write("Ratings DataFrame Columns:", ratings_df.columns)

# Identify the correct common column for merging (replace 'CommonColumn' with the actual common column name)
common_column = 'CommonColumn'  # Replace with the correct column name

# Merge movies_df and ratings_df based on the common column
merged_df = movies_df.merge(ratings_df, on=common_column, how='inner')

# Display recommended movies based on genre
if genre:
    genre = genre.lower()
    recommended_movies = merged_df[merged_df['genres'].str.lower().str.contains(genre)]
    
    if not recommended_movies.empty:
        st.subheader(f"Recommended {genre.capitalize()} Movies with Ratings")
        st.write(recommended_movies)
    else:
        st.warning(f"No {genre.capitalize()} movies found. Try a different genre.")
