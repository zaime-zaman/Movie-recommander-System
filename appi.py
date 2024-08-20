import pickle
import streamlit as st
import requests

# Function to fetch movie poster from API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path

# Function to recommend movies based on similarity
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

# Load movie data and similarity matrix
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Apply custom styles
st.markdown("""
    <style>
    body {
        background-color: #f4f4f9;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .main {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
        max-width: 900px;
        margin: auto;
        text-align: center;
    }
    h1 {
        color: #333333;
        text-align: center;
        font-weight: bold;
        margin-bottom: 40px;
    }
    .stButton button {
        background-color: blue;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 18px;
        font-weight: bold;
        transition: background-color 0.3s ease;
        margin-top: 20px;
    }
    .stButton button:hover {
            color : white;
        background-color: brown;
    }
    .stSelectbox label {
        color: green;
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 10px;
    }
    .stText {
        color: Green;
        font-weight: bold;
        text-align: center;
    }
    .poster {
        border-radius: 10px;
        transition: transform 0.3s ease;
    }
    .poster:hover {
        transform: scale(1.05);
    }
    </style>
    <style>
    @keyframes scale-up {
        0% {
            transform: scale(1);
            color: #FF5733; /* Bright orange color */
        }
        50% {
            transform: scale(1.05);
            color: #FF6F61; /* Slightly different shade for effect */
        }
        100% {
            transform: scale(1);
            color: #FF5733; /* Return to original color */
        }
    }

    .custom-header {
        color: #FF5733; /* Bright orange color */
        font-family: 'Impact', sans-serif; /* Bold and aggressive font family */
        font-size: 48px; /* Larger font size */
        font-weight: bold; /* Bold font */
        text-align: center; /* Center align the header */
        margin-bottom: 20px;
        animation: scale-up 2s ease-in-out infinite; /* Apply scaling animation */
    }
    </style>
    <h1 class="custom-header">🎬 Movie Recommender System</h1>
            <h2 style="color:Black;">By Z.Z Developers</h2> 
""", unsafe_allow_html=True)


# Movie selection dropdown
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Recommendation button and results display
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0], use_column_width=True, caption=recommended_movie_names[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1], use_column_width=True, caption=recommended_movie_names[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2], use_column_width=True, caption=recommended_movie_names[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3], use_column_width=True, caption=recommended_movie_names[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4], use_column_width=True, caption=recommended_movie_names[4])
