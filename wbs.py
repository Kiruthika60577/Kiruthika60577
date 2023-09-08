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

# The rest of your Streamlit app code...
