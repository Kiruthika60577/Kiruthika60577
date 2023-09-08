import streamlit as st
import pandas as pd
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise.prediction_algorithms import KNNBasic

# URLs of your CSV files on GitHub
movies_url = 'https://raw.githubusercontent.com/Kiruthika60577/Kiruthika60577/main/movies.csv'
ratings_url = 'https://raw.githubusercontent.com/Kiruthika60577/Kiruthika60577/main/ratings.csv'

# Streamlit App Header
st.title('Wbsflix Movie Recommendation')

# Load data from GitHub URLs
movies_df = pd.read_csv(movies_url)
ratings_df = pd.read_csv(ratings_url)

# Sidebar for user input
user_id = st.sidebar.text_input('Enter User ID', '1')
selected_genre = st.sidebar.selectbox('Select Genre', movies_df['genres'].unique())

# Button to trigger recommendations
if st.sidebar.button('Get Recommendations'):
    # Filter movies by selected genre
    filtered_movies = movies_df[movies_df['genres'].str.contains(selected_genre)]

    # Load the recommendation model
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(ratings_df[['userId', 'movieId', 'rating']], reader)
    trainset, _ = train_test_split(data, test_size=0.2, random_state=42)
    algo = KNNBasic(sim_options={'name': 'cosine', 'user_based': True})
    algo.fit(trainset)

    # Get movie recommendations for the user
    user_ratings = ratings_df[ratings_df['userId'] == int(user_id)]
    user_unrated_movies = filtered_movies[~filtered_movies['movieId'].isin(user_ratings['movieId'])]
    movie_recommendations = []

    for movie_id in user_unrated_movies['movieId']:
        estimated_rating = algo.predict(int(user_id), movie_id).est
        movie_title = filtered_movies[filtered_movies['movieId'] == movie_id]['title'].values[0]
        movie_recommendations.append((movie_title, estimated_rating))

    # Sort movie recommendations by estimated rating
    movie_recommendations = sorted(movie_recommendations, key=lambda x: x[1], reverse=True)

    # Display recommended movies with ratings
    st.subheader('Recommended Movies with Ratings:')
    for i, (title, estimated_rating) in enumerate(movie_recommendations[:10], start=1):
        st.write(f"{i}. **{title}** (Estimated Rating: {estimated_rating:.2f})")
