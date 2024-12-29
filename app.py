import streamlit as st


from PIL import Image

# Load the image
logo = Image.open('C:\\Users\\user\\Desktop\\greendot app\\logo.png')

# Display the logo with a custom width
st.image(logo, width=500)  # Adjust the width as needed

st.markdown("""
<style>
.custom-logo {
    font-size: 3.4rem;  /* Adjust font size as needed */
    color: #006400;   /* Greendot green (dark green) */
    font-weight: bold;
}
.custom-title {
    font-size: 2.3rem;  /* Adjust font size as needed */
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden}
    header {visibility: hidden}
""", unsafe_allow_html=True)

# Displaying the title with the custom style
st.markdown('<span class="custom-title"><span class="custom-logo">Greendot...</span> Your Path To Technology</span>', unsafe_allow_html=True)

# Add custom CSS for the theme
st.markdown("""
    <style>
        /* Main background color */
        .stApp {
            background-color: lightblack; /* Dark green background */
            color: black;                /* White text */
            secondary-background-color: white;
        }

        /* Style for all text */
        p, h1, h2, h3, h4, h5, h6, li {
            color: white !important;
        }

        /* Style for highlighted text */
        .highlight {
            background-color: black;
            color: white;
            padding: 2px;
        }

        /* Style for markdown text */
        .css-10trblm {
            color: white !important;
        }

        /* Style for buttons */
        .stButton > button {
            background-color: black; /* Darker green for buttons */
            color: white;
            border: 1px solid white;
        }

        /* Button hover effect */
        .stButton > button:hover {
            background-color: #127C56; /* Slightly lighter green on hover */
        }

        /* Container styling */
        .css-1d391kg {
            background-color: #0B6E4F; /* Darker green for containers */
        }

        /* Link color */
        a {
            color: #90EE90 !important; /* Light green for links */
        }
    </style>
""", unsafe_allow_html=True)

about = st.Page(
    page="views/about.py",
    title= 'About US',
    icon = ":material/account_circle:",
    default=True
)

services = st.Page(
    page="views/services.py",
    title= 'Services & Products',
    icon = ":material/radiology:"
)

nav = st.navigation(pages=[about, services])

nav.run()