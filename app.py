import streamlit as st
from googletrans import Translator

st.title("Drama Translation App")

text = st.text_area("Enter text to translate:")
lang = st.text_input("Enter target language code (e.g. 'ur' for Urdu, 'en' for English):")

if st.button("Translate"):
    if text and lang:
        translator = Translator()
        translated = translator.translate(text, dest=lang)
        st.success(translated.text)
    else:
        st.error("Please enter text and language code!")
