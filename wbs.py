import streamlit as st
import pandas as pd


# Upload your data files to your Streamlit app (e.g., using the "Upload File" widget)
uploaded_movies = st.file_uploader("Upload movies.csv", type=["csv"])
uploaded_ratings = st.file_uploader("Upload ratings.csv", type=["csv"])

# Streamlit App Header
st.title('Movie Recommendation App')

# Load data
if uploaded_movies and uploaded_ratings:
    movies_df = pd.read_csv(uploaded_movies)
    ratings_df = pd.read_csv(uploaded_ratings)

    # ... (Rest of the code remains the same as in the previous response)
    
else:
    st.write("Please upload your data files.")

# ... (Rest of the code remains the same as in the previous response)
