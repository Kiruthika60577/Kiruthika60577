import streamlit as st
import pandas as pd

# Streamlit App Header
st.title('Wbsflix')
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wbsflix</title>
    <style>
        body {
            background-image: url('background.jpg'); /* Replace with your image path */
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }
        .streamlit-embed {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
    </style>
</head>
<body>
    <iframe class="streamlit-embed" src="http://localhost:8501" frameborder="0"></iframe>
</body>
</html>



# GitHub repository URL
github_repo_url = 'https://raw.githubusercontent.com/Kiruthika60577/Kiruthika60577/main/'

# URLs of your CSV files on GitHub
movies_url = github_repo_url + 'movies.csv'
ratings_url = github_repo_url + 'ratings.csv'

# Load data from GitHub URLs
movies_df = pd.read_csv(movies_url)
ratings_df = pd.read_csv(ratings_url)

# Sidebar for user input
user_id = st.sidebar.text_input('Enter User ID', '1')
selected_genre = st.sidebar.selectbox('Select Genre', movies_df['genres'].unique())

# Search box for movie titles
search_query = st.sidebar.text_input('Search for Movie', '')

# Filter movies based on search query
filtered_movies = movies_df[movies_df['title'].str.contains(search_query, case=False)]

# Merge filtered_movies with ratings_df to get ratings
filtered_movies_with_ratings = filtered_movies.merge(ratings_df, on='movieId')

# Button to trigger recommendations
if st.sidebar.button('Get Recommendations'):
    # Filter movies by selected genre
    filtered_movies = filtered_movies[filtered_movies['genres'].str.contains(selected_genre)]

    # Load the recommendation model
    # (Assuming you have already loaded and trained the model)

    # Get movie recommendations for the user (similar to your previous code)

# Display the filtered movies with ratings
st.subheader('Filtered Movies with Ratings:')
st.dataframe(filtered_movies_with_ratings[['title', 'rating']])
