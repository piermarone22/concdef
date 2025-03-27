import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



st.set_page_config(layout="wide")
with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

pages = {
    "pages/ever.py": "Evergreen",
    "evergreen.py": "Finanziamento classico"
        }

# Creazione della sidebar con nomi personalizzati
scelta = st.sidebar.radio("Naviga tra le pagine:", list(pages.values()))





st.markdown(
    """
    <style>
        .navbar {
            background-color: #32CD32;
            padding: 10px;
            text-align: center;
            color: white;
            font-size: 30px;
            font-weight: bold;
            border-radius: 5px;
            position: sticky;
            top: 0;
            width: 100%;
            z-index: 1000; /* Impedisce che altri contenuti la coprano */
            box-shadow: 0 4px 2px -2px gray; /* Ombra sotto la navbar */
            display: flex;
            align-items: center;
            justify-content: flex-start;
        }

        .navbar img {
            width: 60px;  /* Aumenta la larghezza dell'immagine */
            height: 60px; /* Aumenta l'altezza dell'immagine */
            margin-right: 20px;  /* Aumenta la distanza tra l'immagine e il testo */
            border-radius: 50%;
        }


        /* Aggiungi un po' di margine superiore al corpo per evitare che la navbar copra il contenuto */
        body {
            margin-top: 80px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Barra di navigazione fissa con immagine a sinistra
st.markdown(
    """
    <div class="navbar">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHleG8EqbuRXokJN0XAx7QQp8E6FFNQOJp-w&s" alt="Logo">Evergreen
    </div>
    """,
    unsafe_allow_html=True
)

st.title("Scelta simulazione")


if st.button("Finanziamento classico"):
        st.switch_page("pages/finanziamento.py")

if st.button("Rinnovo del contantista"):
        st.switch_page("pages/rinnovo.py")