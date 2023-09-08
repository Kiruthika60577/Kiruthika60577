import streamlit as st

# Streamlit App Header
st.title('Wbsflix')

# Create a container for the content with custom CSS
st.markdown(
    """
    <style>
        .container {
            background-color: #141414; /* Netflix background color */
            color: white;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a content container
st.markdown(
    """
    <div class="container">
        <!-- Add your content here -->
        <h2>Welcome to Wbsflix</h2>
        <p>Discover and watch your favorite movies and TV shows.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# The rest of your Streamlit app code...


import streamlit as st
import pandas as pd

# GitHub repository URL
github_repo_url = 'https://raw.githubusercontent.com/Kiruthika60577/Kiruthika60577/main/'

# URLs of your CSV files on GitHub
movies_url = github_repo_url + 'movies.csv'
ratings_url = github_repo_url + 'ratings.csv'

# Streamlit App Header
st.title('Wbsflix Movie Recommendation')

# Load data from GitHub URLs
movies_df = pd.read_csv(movies_url)
ratings_df = pd.read_csv(ratings_url)
import streamlit as st
import pandas as pd

# URLs of your CSV files on GitHub
movies_url = 'https://raw.githubusercontent.com/Kiruthika60577/Kiruthika60577/main/movies.csv'
ratings_url = 'https://raw.githubusercontent.com/Kiruthika60577/Kiruthika60577/main/ratings.csv'

# Streamlit App Header
st.title('Wbsflix Movie Recommendation')

# Load data from GitHub URLs
movies_df = pd.read_csv(movies_url)
ratings_df = pd.read_csv(ratings_url)

# Rest of your Streamlit app code...


