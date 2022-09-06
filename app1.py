import streamlit as st
import joblib

#load the joblib model
model_nb = joblib.load('car_data')

st.title('CAR_DATA PREDICTOR')
ip = st.text_input('Enter your value')

op = model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])
