import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict_genre


# Streamlit UI
st.title("Song Genre Prediction")

# Input for song lyrics
user_input = st.text_area("Enter the song lyrics here:")

if st.button("Predict"):
    if user_input:
        genres = ['Pop', 'Blue', 'Chill', 'Jazz', 'Hip hop', 'Country', 'Rock', 'Soul']
        # Get prediction
        predicted_genre, probabilities = predict_genre(user_input)

        # Display the predicted genre as text
        st.subheader("Predicted Genre:")
        st.write(predicted_genre)

        # Display the probabilities as a bar chart
        st.subheader("Probabilities:")
        df = pd.DataFrame({'Genre': genres, 'Probability': probabilities})
        st.bar_chart(df.set_index('Genre'))

    else:
        st.warning("Please enter song lyrics for prediction.")
