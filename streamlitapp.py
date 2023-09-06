import pandas as pd
url = 'https://drive.google.com/file/d/1fQ4E2q3LKng0ShMswV8kExZJtzfabn-P/view?usp=sharing' # movies.csv
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
movies_df = pd.read_csv(path)
url = 'https://drive.google.com/file/d/1cOW6sRWehqhw8936fFFuSgvkVxVlgyyh/view?usp=sharing' # ratings.csv
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
ratings_df = pd.read_csv(path)
url = 'https://drive.google.com/file/d/1aEracXXZf9HG5U-o_Mw3KX8aaFveiVvR/view?usp=sharing' # links.csv
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
links_df = pd.read_csv(path)
url = 'https://drive.google.com/file/d/1Fc9sf1t5yOR6rgtn-2-EMT5YKw5mReVI/view?usp=sharing' # tags.csv
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
tags_df = pd.read_csv(path)
import streamlit as st
import pandas as pd

# Sample movie data for demonstration
movies_data = pd.DataFrame({
    'Title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'Genre': ['Horror', 'Action', 'Horror', 'Comedy', 'Horror']
})

# Title of your Streamlit app
st.title("WBSFlix - Movie Recommendations")

# Header
st.header("Movie Recommendations")

# Description
st.text("Enjoy personalized movie recommendations!")

# Input for User's Preferred Genre
genre = st.text_input("Enter your preferred movie genre")

# Display recommended movies based on genre
if genre:
    genre = genre.lower()
    recommended_movies = movies_data[movies_data['Genre'].str.lower().str.contains(genre)]
    
    if not recommended_movies.empty:
        st.subheader(f"Recommended {genre.capitalize()} Movies")
        st.write(recommended_movies)
    else:
        st.warning(f"No {genre.capitalize()} movies found. Try a different genre.")

