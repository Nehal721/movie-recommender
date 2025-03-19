import pickle 
import streamlit as st
import requests


st.markdown(
    """
    <style>
        /* Background Image with Light Transparency */
        .stApp {
            background: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), 
                        url("https://wallpapercave.com/wp/wp4770368.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }

        /* Neon Glow Effect on Header */
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #ffcc00; /* Golden text */
            text-shadow: 3px 3px 10px rgba(255, 204, 0, 0.8);
            font-family: 'Cursive', sans-serif;
            text-align: center;
        }

        /* Stylish Movie Button */
        .stButton>button {
            background: linear-gradient(45deg, #ff5733, #c70039);
            color: white !important;
            border: none;
            border-radius: 50px;
            padding: 10px 20px;
            font-size: 18px;
            font-weight: bold;
            transition: 0.3s;
            box-shadow: 0px 0px 15px rgba(255, 87, 51, 0.7);
        }
        .stButton>button:hover {
            background: linear-gradient(45deg, #c70039, #ff5733);
            transform: scale(1.1);
        }

        /* Movie Card Design */
        .stText {
            color: white !important;
            font-size: 20px;
            font-weight: bold;
            text-shadow: 2px 2px 5px rgba(255, 255, 255, 0.7);
        }

        /* Name Tag - Nehal Thakur */
        .name-tag {
            position: fixed;
            bottom: 10px;
            right: 10px;
            background: rgba(0, 0, 0, 0.7);
            color: #ffcc00;
            font-size: 16px;
            font-weight: bold;
            padding: 8px 15px;
            border-radius: 10px;
            text-shadow: 2px 2px 5px rgba(255, 204, 0, 0.8);
            font-family: 'Courier New', monospace;
        }
    </style>
    <div class="name-tag">Made by Nehal Thakur 🎬🔥</div>
    """,
    unsafe_allow_html=True
)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=3595f7c04fd18b0aa64bc6da13a0772d&language=en-US"
    data = requests.get(url)
    data = data.json()
    if 'poster_path' in data and data['poster_path']:
        poster_path = data['poster_path']
        full_path = "http://image.tmdb.org/t/p/w500/" + poster_path
    else:
        full_path = "https://via.placeholder.com/500"  

    return full_path


def recommend (movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])) , reverse = True , key = lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name, recommended_movies_poster

st.header("Movies Recommendation System")
movies =  pickle.load(open('artificats/movies.pkl', 'rb'))
similarity = pickle.load(open('artificats/similarity.pkl', 'rb'))

movie_titles = movies['title'].values

selected_movie = st.selectbox('Type or select a movie:', movie_titles)

if st.button('Show recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])

    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])

    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])
    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])

    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])