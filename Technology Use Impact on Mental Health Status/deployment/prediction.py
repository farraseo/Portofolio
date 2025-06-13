# import libraries
import pandas as pd
import streamlit as st
import pickle

def run():

    # import model
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)

        # variable for client information
    Age = st.number_input(label = 'Input \' Age:', min_value = 0.00)

    Gender = st.selectbox(label = 'Choose \' Gender', options = ['Male', 'Female', 'Other'])

    Technology_Usage_Hours = st.number_input(label = 'Input \' Technology Usage (Hours):', min_value = 0.00)

    Social_Media_Usage_Hours = st.number_input(label = 'Input \' Social Media Usage (Hours)', min_value = 0.00)

    Gaming_Hours = st.number_input(label = 'Input \' Gaming (Hours)', min_value = 0.00)

    Screen_Time_Hours = st.number_input(label = 'Input \' Screen Time (Hours)', min_value = 0.00)

    Stress_Level = st.selectbox(label = 'Input \' Stress Level', options = ['Low', 'Medium', 'High'])

    Sleep_Hours = st.number_input(label = 'Input \' Sleep (Hours)', min_value = 0.00)

    Physical_Activity_Hours = st.number_input(label = 'Input', min_value = 0.00)

    Support_Systems_Access = st.selectbox(label = 'Choose \' Support Systems Access', options = ['Yes', 'No'])

    Work_Environment_Impact = st.selectbox(label = 'Choose \' Work Environment Impact', options = ['Positive', 'Neutral', 'Negative'])

    Online_Support_Usage = st.selectbox(label = 'Choose \' Work Environment Impact', options = ['Yes', 'No'])

    st.write('Customer data from input:')
    # create variable for dataframe
    data = pd.DataFrame({'Age': Age,
                        'Gender': Gender,
                        'Technology_Usage_Hours': Technology_Usage_Hours,
                        'Social_Media_Usage_Hours': Social_Media_Usage_Hours,
                        'Gaming_Hours': Gaming_Hours,
                        'Screen_Time_Hours': Screen_Time_Hours,
                        'Stress_Level': Stress_Level,
                        'Sleep_Hours': Sleep_Hours,
                        'Physical_Activity_Hours': Physical_Activity_Hours,
                        'Support_Systems_Access': Support_Systems_Access,
                        'Work_Environment_Impact': Work_Environment_Impact,
                        'Online_Support_Usage': Online_Support_Usage}, index = [0])
    
    df = data.copy()
    df = df[['Age', 'Gender', 'Technology_Usage_Hours', 'Social_Media_Usage_Hours', 'Gaming_Hours', 'Screen_Time_Hours',
             'Stress_Level', 'Sleep_Hours', 'Physical_Activity_Hours', 'Support_Systems_Access', 'Work_Environment_Impact',
             'Online_Support_Usage']]
    
        # display dataframe
    st.dataframe(data)
    
    if st.button(label = 'predict'):
        y_pred_inf = model.predict(data)
        if y_pred_inf[0] == 0:
            st.write('Client is Excellent')
        elif y_pred_inf[0] == 1:
            st.write('Client is Fair')
        elif y_pred_inf[0] == 2:
            st.write('Client is Good')
        elif y_pred_inf[0] == 3:
            st.write('Client is Poor')


if __name__=='__main__':
    run()