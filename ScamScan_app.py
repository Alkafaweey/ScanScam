import joblib
import re
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st

header = st.container()
with header:
    st.title("Welcome to ScamScan")
    st.write("ScamScan is a machine learning model, built for classifying spam and not spam contents in a message")


message_text = st.text_input("Enter a message for spam evaluation")

def preprocessor(text):
    text = re.sub('<[^>]*>', '', text) 
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')
    return text
model = joblib.load('Scanscam.joblib')

def classify_message(model, message):
    label = model.predict([message])[0]
    return {'This message is': label}

if message_text != '':
  result = classify_message(model, message_text)
  st.write(result)