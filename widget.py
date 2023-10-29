import streamlit as st
import datetime
import pandas as pd

# ====== INPUT WIDGET ======

# text_input()
name = st.text_input(label="Nama Lengkap", value="")
st.write('Nama: ', name)

# text_area()
text = st.text_area("Feedback")
st.write("text: ", text)

# number_input()
number = st.number_input(label="Umur")
st.write("Umur: ", int(number), " Tahun")

# date_input()
date = st.date_input(label="Tanggal Lahir", min_value=datetime.date(1900, 1, 1))
st.write("Tanggal Lahir: ", date)

# file_uploader()
uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

# camera_input()
# picture = st.camera_input("Take a picture")
# if picture:
    # st.image(picture)

# ====== BUTTON WIDGET =======

# button()
if st.button("Say Hello"):
    st.write("Hello There")

# checkbox()
agree = st.checkbox("I Agree")

if agree:
    st.write("Welcome to family")

# radio()
genre = st.radio(
    label="What's your favorite movie genre",
    options=("Comedy", "Drama", "Action"),
    horizontal=False
)

# selectbox()
genre_film = st.selectbox(
    label="Select your favorite film",
    options=("Action", "Romance", "Drama", "Fiction")
)

# multiselect()
genre_multy = st.multiselect(
    label="Select your Favorite film",
    options=("Action", "Drama", "Romance", "Horor", "Thriller")
)
st.write(genre_multy)

# slider()
values = st.slider(
    label="Select a range value",
    min_value=0,
    max_value=100,
    value=(0, 100)
)
st.write(values)
