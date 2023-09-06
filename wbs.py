import streamlit as st
import pandas as pd
from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
pip install scikit-surprise

# Set a background image for the Streamlit app
st.markdown(
    """
    <style>
    body {
        background-image: url("https://yourdomain.com/assets/netflix_bg.jpg");  /* Replace with the actual URL of your image */
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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

# Filter movies by genre
genre = st.sidebar.selectbox('Select a Genre', movies_df['genres'].unique())
filtered_movies = movies_df[movies_df['genres'].str.contains(genre)]

# Display filtered movies and their ratings
st.subheader(f'Movies in the "{genre}" Genre:')
for index, row in filtered_movies.iterrows():
    st.write(f"**{row['title']}** (Genres: {row['genres']})")

    # Get the average rating for this movie
    movie_ratings = ratings_df[ratings_df['movieId'] == row['movieId']]['rating']
    average_rating = movie_ratings.mean()
    
    # Display the movie poster if a valid URL is available
    poster_url = row['poster_url']  # Replace with the actual column name containing poster URLs
    if poster_url and isinstance(poster_url, str) and poster_url.startswith(('http://', 'https://')):
        st.image(poster_url, caption=row['title'], use_column_width=True)
    else:
        st.write("No poster available")
    
    st.write(f"Average Rating: {average_rating:.2f}")

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
    poster_url = movie_info['poster_url'].values[0]  # Replace with the actual column name containing poster URLs
    st.write(f"{i}. **{title}** (Genres: {genres}), Estimated Rating: {estimated_rating:.2f}")
    
    # Display the movie poster if a valid URL is available
    if poster_url and isinstance(poster_url, str) and poster_url.startswith(('http://', 'https://')):
        st.image(poster_url, caption=title, use_column_width=True)
    else:
        st.write("No poster available")
