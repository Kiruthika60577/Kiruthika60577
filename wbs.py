import streamlit as st

# Streamlit App Header
st.title('Wbsflix')

# Define the URL of your background image
background_image_url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.slashgear.com%2Fnetflix-4k-streaming-on-macos-big-sur-to-require-a-t2-security-chip-02640845%2F&psig=AOvVaw0Zg5pd4ZMy4kUBAo3njC4R&ust=1694242050286000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCIjdhs-1moEDFQAAAAAdAAAAABAE'

# Create a custom CSS style to set the background image
background_style = f"""
    <style>
        body {{
            background-image: url('{background_image_url}');
            background-size: cover;
        }}
    </style>
"""

# Apply the custom CSS style
st.markdown(background_style, unsafe_allow_html=True)

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


