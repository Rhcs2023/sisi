import streamlit as st

# Diccionario con palabras a traducir
diccionario = {
    "hello": "hola",
    "world": "mundo",
    "good": "bueno",
    "morning": "mañana"
}

def traducir_oracion(oracion):
    palabras = oracion.split()
    oracion_traducida = " ".join([diccionario.get(palabra.lower(), palabra) for palabra in palabras])
    return oracion_traducida

st.title("Traductor de Palabras")

# Preguntar al usuario por una oración en inglés
oracion = st.text_input("Ingresa una oración en inglés:")

if st.button("Traducir"):
    oracion_traducida = traducir_oracion(oracion)
    st.write(f"La oración traducida al español es: {oracion_traducida}")
