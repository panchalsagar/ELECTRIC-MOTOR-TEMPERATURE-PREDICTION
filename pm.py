# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('reg.pkl', 'rb') 
reg = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(ambient,stator_tooth,coolant,motor_speed):   
 
    # Making predictions 
    prediction = reg.predict( 
        [[ambient,stator_tooth,coolant,motor_speed]])
     
    return prediction
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Temperature Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    ambient = st.number_input('Enter ambient temperature')
    stator_tooth = st.number_input('Enter stator_tooth temperature') 
    coolant = st.number_input("Enter coolant temperature") 
    motor_speed = st.number_input("Enter motor_speed")
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(ambient,stator_tooth,coolant,motor_speed) 
        st.success('PM temperature is {}'.format(result))
        print(result)
     
if __name__=='__main__': 
    main()
