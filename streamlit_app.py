import streamlit as st
from PIL import Image

logo = Image.open("Logo.jpg")
st.image(logo, width=200)
st.title("CyBuy")
st.header("Welcome to CyBuy— where your security comes first.")

email = st.text_input('Your Email', 'Enter your email')
manufacturer = st.text_input('Device Manufacturer', 'Enter the device manufacturer, i.e. "Apple"')
product = st.text_input('Product Name', 'Enter the product name, i.e. "iPhone 13"')

# if user attempts to submit form without an email address, return an error message
questionnaireScore = 0

q1 = st.radio(
     "1) Is your device connected to a public or private network?",
     ('Public', 'Private'))
if q1 == 'Public':
    questionnaireScore += 2

q2 = st.radio(
     "2) Do you store data on a cloud or conduct any sort of distributed computing?",
     ('Yes', 'No'))
if q2 == 'Yes':
    questionnaireScore += 2

q3 = st.radio(
    "3) Do you work from home?",
    ('Yes', 'No'))
if q3 == 'Yes':
    questionnaireScore += 2

q4 = st.radio(
    "4) Are you an IOT nerd? Do you have smart devices in your home like Amazon Alexa or Google Home?",
    ('Yes', 'No'))
if q4 == 'Yes':
    questionnaireScore += 2

q5 = st.radio(
    "5) Do you use any sort of antivirus software such as Norton, Bitdefender, or McAfee?",
    ('Yes', 'No'))
if q4 == 'No':
    questionnaireScore += 2