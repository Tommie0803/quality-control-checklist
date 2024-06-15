import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title(" Neurosurgery Quality Control")

st.title("Daily Checks")

st.selectbox('THEATRE',['Neuro G1','Neuro G2','Neuro G3','Theatre 4','Theatre 7','Neuro Angio','MRI 1','MRI 2','Others'])

st.text_input("Others",placeholder = "Description")

st.title('Checks')

st.warning('Click the checkbox to confirm')

st.checkbox('Anaesthetic machine')

st.checkbox('Difficult Airway Trolley Adult')

st.checkbox('Difficult Airway Trolley Paed')

st.checkbox('Drug fridge')

st.checkbox('Drug fridge Exparrel G2')

st.checkbox('Anaesthetic Daily checks')

st.checkbox('Scrub Daily Checks')

st.checkbox('BM Machine')

st.checkbox('Paediatric Trolley')

st.title('Anaesthetic Nurse or ODP')

st.checkbox('Damp dusting done')

st.checkbox('Emergency Button')

st.checkbox('CD Ordered')

st.checkbox('Theatre ready for Next day')

st.checkbox('Pharmacy orders')

st.checkbox('Emergency Exit')

st.text_input("Report",placeholder = "Adverse or Repair")

st.text_area('Description')

st.sidebar.date_input('Date')

st.sidebar.time_input('Time')

st.sidebar.text_input("Name",placeholder = "Barak Obama")

if st.button('Submit'):
    st.write('Thank you for submitting')
    


