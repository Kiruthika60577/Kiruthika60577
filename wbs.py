import streamlit as st
import pandas as pd
from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split

# Load data from GitHub (replace with your GitHub URLs)
movies_url = 'https://raw.githubusercontent.com/kiruthika60577/wbs.py/main/movies.csv'
ratings_url = 'https://raw.githubusercontent.com/kiruthika60577/wbs.py/main/ratings.csv'

# Load and preprocess data
movies_df = pd.read_csv(movies_url)
ratings_df = pd.read_csv(ratings_url)

# Streamlit App Header
st.title('Movie Recommendation App')

# User Input
user_id = st.text_input('Enter User ID')
selected_genre = st.selectbox('Select Movie Genre', movies_df['genres'].unique())

# Load the recommendation model and make predictions
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(ratings_df[['userId', 'movieId', 'rating']], reader)
trainset, testset = train_test_split(data, test_size=0.2, random_state=142)
algo = KNNBasic(sim_options={'name': 'cosine', 'user_based': True})
algo.fit(trainset)
testset = trainset.build_anti_testset()
predictions = algo.test(testset)

# Generate movie recommendations based on user input
user_recommendations = []

for uid, iid, true_r, est, _ in predictions:
    if int(user_id) == uid and selected_genre in movies_df[movies_df['movieId'] == iid]['genres'].values[0]:
        user_recommendations.append((iid, movies_df[movies_df['movieId'] == iid]['title'].values[0], est))

# Display recommendations
st.subheader('Movie Recommendations:')
for movie_id, title, estimated_rating in user_recommendations:
    st.write(f"Movie ID: {movie_id}, Title: {title}, Estimated Rating: {estimated_rating:.2f}")
