# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:24:30 2023

@author: ssup1
"""

import numpy as np
import pickle
import streamlit as st
import pandas as pd

loadedmodel = pickle.load(open('C:/Users/ssup1/Downloads/endtoend/trained.sav', 'rb'))



# Define the features and user inputs as you did in the original code
features = ['Frequency [Classical]', 'Frequency [Country]', 'Frequency [EDM]', 'Frequency [Folk]', 'Frequency [Gospel]', 
            'Frequency [Hiphop]', 'Frequency [Jazz]', 'Frequency [Kpop]', 'Frequency [Latin]', 'Frequency [Lofi]', 
            'Frequency [Metal]', 'Frequency [Pop]', 'Frequency [RnB]', 'Frequency [Rap]', 'Frequency [Rock]', 
            'Frequency [Videogamemusic]', 'Anxiety', 'Depression', 'Insomnia', 'OCD']
#Creating function

def predict_genre(user_inputs):
    # User inputs for the survey dataset
    user_df = pd.DataFrame([user_inputs], columns=features)

    # Make predictions for the user's favorite genre
    predicted_label = loadedmodel.predict(user_df)[0]
    
    # Define the genre map as in the original code
    genre_map = {'Video game music': 0, 'Jazz': 1, 'R&B': 2, 'K pop': 3, 'Rock': 4, 'Country': 5, 'EDM': 6, 'Pop': 7, 'Hip hop': 8, 'Rap': 9, 'Classical': 10, 'Metal': 11, 'Folk': 12, 'Lofi': 13, 'Gospel': 14, 'Latin': 15}


    # Map the integer predicted_label to its corresponding categorical string value
    predicted_genre = list(genre_map.keys())[list(genre_map.values()).index(predicted_label)]

    # Create the recommended sentence
    recommended_sentence = f"You might want to listen to {predicted_genre} to bring your spirits up :D"
    
    return recommended_sentence


def main():
    st.title("Music Genre for mental health")
    
    
    Classical = st.text_input("Please rate on a scale of 0-3, how much do you listen to the music of genre 'Classical'?")
    Country = st.text_input("Please rate on a scale of 0-3, how much do you listen to the music of genre 'Country'?")
    EDM = st.text_input("Please rate on a scale of 0-3, how much do you listen to the music of genre 'EDM'?")
    Folk = st.text_input("Please rate on a scale of 0-3, how much do you listen to the music of genre 'Folk'?")
    Gospel = st.text_input("Please rate on a scale of 0-3, how much do you listen to the music of genre 'Gospel'?")
    Hiphop= st.text_input("Please rate on a scale of 0-3, how much do you listen to the music of genre 'Hiphop'?")
    Jazz= st.text_input("Please rate on a scale of 0-3, how much do you listen to the music of genre 'Jazz'?")
    Kpop = st.text_input("Please rate on a scale of 0-3, how much do you listen to the music of genre 'Kpop'?")
    Latin= st.text_input("Please rate on a scale of 0-3, how much do you listen to the music of genre 'Latin'?")
    Lofi= st.text_input("Please rate on a scale of 0-3, how much do you listen to the music of genre 'Lofi'?")
    Metal = st.text_input("Please rate on a scale of 0-3, how much do you listen to the music of genre 'Metal'?")
    Pop=st.text_input("Please rate on a scale of 0-3, how much do you listen to the music of genre 'Pop'?")
    RnB = st.text_input("Please rate on a scale of 0-3, how much do you listen to the music of genre 'RnB'?")
    Rap = st.text_input("Please rate on a scale of 0-3, how much do you listen to the music of genre 'Rap'?")
    Rock = st.text_input("Please rate on a scale of 0-3, how much do you listen to the music of genre 'Rock'?")
    Videogamemusic = st.text_input("Please rate on a scale of 0-3, how much do you listen to the music of genre 'Videogamemusic'?")
    Anxiety =  st.text_input("Please rate your feelings for Anxiety on a scale of 0-10")
    Depression=st.text_input("Please rate your feelings for Depression on a scale of 0-10")
    Insomnia = st.text_input("Please rate your feelings for Insomnia on a scale of 0-10")
    OCD = st.text_input("Please rate your feelings for OCD on a scale of 0-10")
    
    
    health = ''
    
    if st.button('Your music recommendation'):
        health = predict_genre([Classical,Country,EDM,Folk,Gospel,Hiphop,Jazz,Kpop,Latin,Lofi,Metal,Pop,
                                RnB,Rap,Rock,Videogamemusic,Anxiety,Depression,Insomnia,OCD])
        
        
    
    

    st.success(health)
    
if __name__ == '__main__':
    main()
    
    

    
   
    
    
    
    
    
    
    



    