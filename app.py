import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image
import io
#https://api.themoviedb.org/3/movie/1363?api_key=99119c5f84aa49c920ff1afe804f32e0&language=en-US
#this was the api key i generated from tmdb where 1363 is {movie_id} and
#99119c5f84aa49c920ff1afe804f32e0 this was my personal api key of tmdb website of username saandhil
#password and mail id in phone
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=99119c5f84aa49c920ff1afe804f32e0&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_dict = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies_names = []
    recommended_movies_posters = []

    for i in movies_dict:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_names.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies_names,recommended_movies_posters

movies_dict = pickle.load(open('Movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie-Recommender-System')
selected_movie_name = st.selectbox(
'what you will recommend',
movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # Create five columns using st.columns
    col1, col2, col3, col4, col5 = st.columns(5)

    # Display name and poster in each column
    with col1:
        st.write(names[0])
        response = requests.get(posters[0])
        image = Image.open(io.BytesIO(response.content))
        st.image(image, use_column_width=True)

    with col2:
        st.write(names[1])
        response = requests.get(posters[1])
        image = Image.open(io.BytesIO(response.content))
        st.image(image, use_column_width=True)

    with col3:
        st.write(names[2])
        response = requests.get(posters[2])
        image = Image.open(io.BytesIO(response.content))
        st.image(image, use_column_width=True)

    with col4:
        st.write(names[3])
        response = requests.get(posters[3])
        image = Image.open(io.BytesIO(response.content))
        st.image(image, use_column_width=True)

    with col5:
        st.write(names[4])
        response = requests.get(posters[4])
        image = Image.open(io.BytesIO(response.content))
        st.image(image, use_column_width=True)
