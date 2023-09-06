import streamlit as st
import pandas as pd
from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy
from surprise.model_selection import cross_validate

# Load the preprocessed data
movies_df = pd.read_csv('movies.csv')
ratings_df = pd.read_csv('ratings.csv')

# Function to get top movie recommendations for a user
def get_top_n(predictions, user_id, n=10):
    user_recommendations = []
    for uid, iid, true_r, est, _ in predictions:
        if user_id == uid:
            user_recommendations.append((iid, est))
    ordered_recommendations = sorted(user_recommendations, key=lambda x: x[1], reverse=True)
    return ordered_recommendations[:n]

# Streamlit App Header
st.title('Wbsflix Movie Recommendation App')

# Sidebar for user input
user_id = st.sidebar.text_input('Enter User ID', '1')

# Load the recommendation model and make predictions
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(ratings_df[['userId', 'movieId', 'rating']], reader)
trainset, testset = train_test_split(data, test_size=0.2, random_state=142)
algo = KNNBasic(sim_options={'name': 'cosine', 'user_based': True})
algo.fit(trainset)
testset = trainset.build_anti_testset()
predictions = algo.test(testset)
top_n = get_top_n(predictions, int(user_id))

# Display movie recommendations
st.subheader('Top Movie Recommendations:')
for i, (movie_id, estimated_rating) in enumerate(top_n, start=1):
    movie_info = movies_df[movies_df['movieId'] == movie_id]
    title = movie_info['title'].values[0]
    genres = movie_info['genres'].values[0]
    st.write(f"{i}. **{title}** (Genres: {genres}), Estimated Rating: {estimated_rating:.2f}")

