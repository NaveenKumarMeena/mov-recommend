import streamlit as st
import pickle
import pandas as pd
import requests



def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster
add_bg_from_url()
movies_dict = pickle.load(open('movie_dict.pkl' , 'rb'))
movies = pd.DataFrame(movies_dict)

similarity =pickle.load(open('similarity.pkl' , 'rb'))

st.title('Movie Recommender System')
selected_movies = st.selectbox(
'Select Movie',
movies['title'].values)

if st.button('Recommend'):
   names,poster =  recommend(selected_movies)
   col1, col2, col3,col4,col5 = st.columns(5)

   with col1:
       st.text(names[0])
       st.image(poster[0])

   with col2:
       st.text(names[1])
       st.image(poster[1])

   with col3:
    st.text(names[2])
    st.image(poster[2])

   with col4:
        st.text(names[3])
        st.image(poster[3])

   with col5:
       st.text(names[4])
       st.image(poster[4])
