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
            st.write(f"{i}. **{title}** (Estimated Rating: {estimated_rating:.2f}")
        
else:
    st.write("Please upload your data files.")

# ... (Rest of the code remains the same as in the previous response)
