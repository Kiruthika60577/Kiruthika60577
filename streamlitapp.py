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

# File uploader widget for uploading a dataset
uploaded_file = st.file_uploader("Upload your movie dataset (CSV or Excel)", type=["csv", "xlsx"])

# Load movies.csv from Google Drive
movies_url = 'https://drive.google.com/file/d/1fQ4E2q3LKng0ShMswV8kExZJtzfabn-P/view?usp=sharing'
movies_path = 'https://drive.google.com/uc?export=download&id=' + movies_url.split('/')[-2]
movies_df = pd.read_csv(movies_path)

# Load ratings.csv from Google Drive
ratings_url = 'https://drive.google.com/file/d/1cOW6sRWehqhw8936fFFuSgvkVxVlgyyh/view?usp=sharing'
ratings_path = 'https://drive.google.com/uc?export=download&id=' + ratings_url.split('/')[-2]
ratings_df = pd.read_csv(ratings_path)

# Load links.csv from Google Drive
links_url = 'https://drive.google.com/file/d/1aEracXXZf9HG5U-o_Mw3KX8aaFveiVvR/view?usp=sharing'
links_path = 'https://drive.google.com/uc?export=download&id=' + links_url.split('/')[-2]
links_df = pd.read_csv(links_path)

# Load tags.csv from Google Drive
tags_url = 'https://drive.google.com/file/d/1Fc9sf1t5yOR6rgtn-2-EMT5YKw5mReVI/view?usp=sharing'
tags_path = 'https://drive.google.com/uc?export=download&id=' + tags_url.split('/')[-2]
tags_df = pd.read_csv(tags_path)

# Display recommended movies based on genre
if genre:
    genre = genre.lower()
    recommended_movies = movies_df[movies_df['Genre'].str.lower().str.contains(genre)]
    
    if not recommended_movies.empty:
        st.subheader(f"Recommended {genre.capitalize()} Movies")
        st.write(recommended_movies)
    else:
        st.warning(f"No {genre.capitalize()} movies found. Try a different genre.")
