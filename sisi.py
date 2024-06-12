import streamlit as st
from googletrans import Translator

translator = Translator()

# Diccionario con palabras a traducir
diccionario = {
    "hello": "hola",
    "world": "mundo",
    "good": "bueno",
    "morning": "mañana"
}

st.title("Traductor de Inglés a Español")

# Preguntar al usuario por una oración en inglés
sentence = st.text_input("Ingresa una oración en inglés:")

if st.button("Traducir"):
    words = sentence.split()
    translated_sentence = " ".join([diccionario.get(word.lower(), word) for word in words])
    
    st.write(f"La oración traducida al español es: {translated_sentence}")