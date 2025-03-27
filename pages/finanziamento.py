import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



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



st.title("Finanziamento classico")

st.subheader("Inserisci i dati per calcolare i costi totali")

col1,col2,col3 = st.columns(3)
with col1:
    st.title("Rata")
with col2:
    st.session_state["rata"] = st.number_input("",min_value=0, step=10)
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
    impre = st.number_input("Imprevisti", min_value=0, step=50)

with col2:
    st.write("")
    st.write("")
    st.metric("💵 Totale Imprevisti", f"{impre:,.2f} €")


totale = spesa_ass + spesa_manu + spesa_gomme + impre

with col3:
    st.write("") 
    st.write("")
    st.metric("TOTALE", f"{totale:,.2f} €") 


tot_mese = round(totale / anni_ass / 12)

anni_ass = int(anni_ass)
st.header("Costi di guida")

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    st.metric("TOTALE COSTI", f"{totale:,d} €")

with col2:
    st.header("/")

with col3:
    st.metric("ANNI", f"{anni_ass:,d}")

with col4:
    st.header("=")

with col5:
    st.metric("TOTALE AL MESE",f"{tot_mese:,.2f} €")



st.session_state['tot_tot'] = st.session_state['rata'] + tot_mese


# Divider personalizzato
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

st.title("Quanto sarà la mia rata?")

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    st.metric("RATA", f"{st.session_state["rata"]:,.2f} €")

with col2:
    st.header("+")

with col3:
    st.metric("COSTI DI GUIDA",f"{tot_mese:,.2f} €")

with col4:
    st.header("=")

with col5:
    st.metric("TOTALE AL MESE",f"{st.session_state["tot_tot"]:,.2f} €")

st.metric("", f"💵 Spenderai quindi {st.session_state["tot_tot"]:,.2f} € al mese.")


df = pd.DataFrame({
    "Voce di Spesa": ["Assicurazioni", "Manutenzioni", "Gomme", "Imprevisti"],
    "Totale (€)": [spesa_ass, spesa_manu, spesa_gomme, impre]
})


if st.button("CONFRONTA CON EVERGREEN"):
        st.switch_page("pages/ever.py")


with st.expander("Visualizza grafico"):
    st.subheader("📈 Distribuzione Costi")
    fig, ax = plt.subplots()
    ax.bar(df["Voce di Spesa"], df["Totale (€)"], color=['lightblue', 'teal', 'mediumseagreen', 'forestgreen'])
    ax.set_ylabel("Costo (€)")
    ax.set_facecolor((0,0,0,0))
    fig.patch.set_alpha(0)
    ax.tick_params(colors='white')  # Numeri sugli assi bianchi
    ax.yaxis.label.set_color('white')  # Etichetta asse Y bianca
    ax.xaxis.label.set_color('white')  # Etichetta asse X bianca
    ax.spines['bottom'].set_color('white')  # Bordo inferiore bianco
    ax.spines['left'].set_color('white')  # Bordo sinistro bianco
    st.pyplot(fig)



