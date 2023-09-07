import streamlit as st
import pandas as pd


# Upload your data files to your Streamlit app (e.g., using the "Upload File" widget)
uploaded_movies = st.file_uploader("Upload movies.csv", type=["csv"])
uploaded_ratings = st.file_uploader("Upload ratings.csv", type=["csv"])

# Streamlit App Header
st.title('Wbsflix Movie Recommendation')

# Load data
if uploaded_movies and uploaded_ratings:
    movies_df = pd.read_csv(uploaded_movies)
    ratings_df = pd.read_csv(uploaded_ratings)

    # Sidebar for user input
    user_id = st.sidebar.text_input('Enter User ID', '1')

    # Filter movies by genre
    selected_genre = st.sidebar.selectbox('Select Genre', movies_df['genres'].unique())
    filtered_movies = movies_df[movies_df['genres'].str.contains(selected_genre)]

    # ... (Rest of the code remains the same as in the previous response)
    
else:
    st.write("Please upload your data files.")

# ... (Rest of the code remains the same as in the previous response)

