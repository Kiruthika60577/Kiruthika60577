
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

