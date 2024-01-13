import streamlit as st
import numpy as np
import pandas as pd
import pickle
import sklearn




model = pickle.load(open('Absentmodel.pkl', 'rb'))

st.title('Absenteeism at work Prediction')




def user_report():
    EmployeeNumber = st.text_input('EmployeeNumber')
    Surname = st.text_input('Surname')
    GivenName = st.text_input('GivenName')
    City = st.text_input('City')
    JobTitle = st.text_input('JobTitle')
    StoreLocation = st.text_input('StoreLocation')
    LengthService = st.text_input('LengthService')
    Age = st.text_input('Age')
    
    


    user_report_data = {
    'EmployeeNumber':EmployeeNumber,
    'Surname':Surname,
    'GivenName':GivenName,
    'City':City,
    'JobTitle':JobTitle,
    'StoreLocation':StoreLocation,
    'LengthService':LengthService,
    'Age':Age
    
        
    }   
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data


user_data = user_report() 

if st.button("predict"):
     model.predict(user_data)
     st.write(model.predict(user_data))




