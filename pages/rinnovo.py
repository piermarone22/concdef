import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np


st.set_page_config(layout="wide")
with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)





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
st.title("Pagamento con bonifico")
st.write("")
st.write("")

st.subheader("Inserisci i dati per calcolare i costi totali")

col1,col2,col3 = st.columns(3)
with col1:
    st.title("Prezzo dell'auto")
with col2:
    prezzo = st.number_input("",min_value=0, step=10)

st.write("")
st.write("")
st.write("")
st.markdown(
    """
    <style>
        .custom-divider {
            border-top: 2px solid #32CD32;  /* Colore personalizzato del divider (arancione) */
            margin: 20px 0;  /* Aggiungi spazio sopra e sotto il divider */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Divider personalizzato
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

st.header("Quali sono i costi che dovrò affrontare?")

col1,col2,col3 = st.columns(3)

with col1:
    assicurazione = st.number_input("Assicurazione", min_value=0, step=50)
with col2:
    anni_ass = st.slider("Anni", min_value=1, max_value=20)

spesa_ass = assicurazione * anni_ass

with col3:
    st.write("")
    st.write("")
    st.metric("💵 Totale Assicurazioni", f"{spesa_ass:,.2f} €")
col1,col2,col3 = st.columns(3)

with col1:
    manu = st.number_input("Manutenzioni", min_value=0, step=50)

with col2:
    anni_manu = st.slider("Anni", min_value=1, max_value=20, key="slidermanu")

spesa_manu = manu * anni_manu

with col3:
    st.write("")
    st.write("")
    st.metric("💵 Totale Manutenzioni", f"{spesa_manu:,.2f} €")

col1,col2,col3 = st.columns(3)
with col1:
    gomme = st.number_input("Gomme", min_value=0, step=50)

with col2:
    anni_gomme = st.slider("Numero di treni", min_value=1, max_value=20, key="slidergomme")

spesa_gomme = gomme * anni_gomme

with col3:
    st.write("")
    st.write("")
    st.metric("💵 Totale Gomme", f"{spesa_gomme:,.2f} €")

col1,col2,col3 = st.columns(3)

with col1:
    impre = st.number_input("Extra", min_value=0, step=50)

with col2:
    st.write("")
    st.write("")
    st.metric("💵 Totale Extra", f"{impre:,.2f} €")


totale = spesa_ass + spesa_manu + spesa_gomme + impre

with col3:
    st.write("") 
    st.write("")
    st.metric("TOTALE", f"{totale:,.2f} €") 


tot_mese = round(totale / anni_ass / 12)

anni_ass = int(anni_ass)
st.header(f"Dopo {anni_ass} anni ho speso...")

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
   st.metric("COSTI TOTALI", f"{totale:,d} €") 

with col2:
    st.header("+")

with col3:
    st.metric("PREZZO DELL'AUTO", f"{prezzo:,d} €")

with col4:
    st.header("=")

totals = totale + prezzo

with col5:
    st.metric("TOTALE", f"{totals:,d} €")

st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

st.header("Accantonamento e costo di guida")
st.write("")

col1,col2,col3, col4, col5 = st.columns(5)

with col1:
    st.write("")
    st.subheader(f"Tra {anni_ass} anni")

with col2:
    valore_nuova = st.number_input("Valore dell'auto nuova", min_value=0, step=100)

with col3:
    valore_vecchia = st.number_input("Valore della mia macchina", min_value=0, step=100)

cifra = valore_nuova - valore_vecchia
with col5:
    st.metric("Cifra da risparmiare", f"{cifra:,d} €",f"{valore_nuova}-{valore_vecchia}", delta_color="inverse")






####
st.header("Costi mensili dell'auto")

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
   st.metric("COSTI DI GUIDA", f"{tot_mese:,d} €",f"{totale} / {anni_ass} / 12", delta_color="inverse") 

with col2:
    st.header("+")

cifra_mese = cifra / anni_ass / 12
with col3:
    st.metric("CIFRA DA RISPARMIARE", f"{int(cifra_mese):,d} €", f"{cifra} / {anni_ass} / 12", delta_color="inverse")

with col4:
    st.header("=")

totale_tot = tot_mese + cifra_mese

with col5:
    st.metric("TOTALE", f"{int(totale_tot):,d} €")

st.write("")
st.write("")

st.markdown(
    """
    <style>
        .custom-divider2 {
            border-top: 20px solid #32CD32;  /* Colore personalizzato del divider (arancione) */
            margin: 20px 0;  /* Aggiungi spazio sopra e sotto il divider */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Divider personalizzato
st.markdown('<div class="custom-divider2"></div>', unsafe_allow_html=True)

st.write("")


st.title("Operazione Evergreen")

col1,col2,col3 = st.columns(3)
with col1:
    anticipo = st.number_input("Anticipo",min_value=0, step=10)
with col2:
    mensili = st.number_input("Mensilità",min_value=0, step=10)
with col3:
    mesi_ever = st.slider("Mesi", min_value=12, max_value=60, value=12, step=12)
st.header("Costo dell'operazione")

tot_op = anticipo + (mensili * mesi_ever)
st.metric("COSTO TOTALE EVERGREEN", f"{int(tot_op):,d} €")

col1,col2,col3 = st.columns(3)

with col1:
    st.header("Evergreen")
    st.header(f"{tot_op} €")

with col2:
    st.header("Classico")
    st.header(f"{totals} €")

with col3:
    st.header("Confronto")
    st.header(f"{int(((totals /anni_ass / 12) * mesi_ever) - tot_op)} €")

riga1 = "La voce “Confronto” è la differenza in spesa che si avrebbe scegliendo il pagamento classico rispetto all’Evergreen."
riga2 = "(pagamento classico / totale anni / 12 x mesi evergreen) - costo operazione evergreen"

st.text(f"{riga1}\n{riga2}")


# Parametri principali
anni_ass = int(anni_ass)  # Numero di anni
mesii = anni_ass * 12  # Numero totale di mesi
totale_tot = tot_mese + cifra_mese  # Costo totale mensile incluso la cifra da risparmiare

# ✅ Creazione del vettore per il pagamento classico
mesi_classici = np.arange(1, mesii + 1, 1)  # Crea una lista dei mesi da 1 a mesii
vettore_classico = np.array([totale_tot * i for i in mesi_classici])  # Moltiplica totale_tot per il numero del mese

df_classico = pd.DataFrame({
    "Mese": mesi_classici,
    "Costo (€)": vettore_classico,
    "Tipo": ["Classico"] * len(mesi_classici)
})

# ✅ Creazione del vettore per il modello Evergreen
mesi_evergreen = np.arange(1, mesi_ever + 1, 1)  # Ora ha una progressione reale
vettore_evergreen = np.cumsum([tot_op / mesi_ever] * mesi_ever)  # Anche questo cresce nel tempo

df_evergreen = pd.DataFrame({
    "Mese": mesi_evergreen,
    "Costo (€)": vettore_evergreen,
    "Tipo": ["Evergreen"] * len(mesi_evergreen)
})

# ✅ Unione dei due DataFrame
df_finale = pd.concat([df_classico, df_evergreen], ignore_index=True)

# ✅ Creazione del grafico
fig = px.line(df_finale, x="Mese", y="Costo (€)", color="Tipo", markers=True, title="Confronto Classico vs. Evergreen", color_discrete_map={"Classico": "red", "Evergreen": "green"})

# ✅ Mostrare in Streamlit
st.plotly_chart(fig)


st.header("Interesse composto")
col1, col2, col3 = st.columns(3)
with col1:
    cap = st.number_input("Capitale", step = 100)
with col2:
    intere = st.number_input("Interesse", min_value=0, max_value=100)
with col3:
    tempo = st.number_input("Tempo",min_value = 0)

intcomp = cap * (1+(intere/100))** tempo 
st.metric("Interesse composto", f"{intcomp}")

