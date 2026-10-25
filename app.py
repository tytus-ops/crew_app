import streamlit as st
import random
import time
st.set_page_config(page_title="The Crew", page_icon="🚀")



st.title("The Crew App")
palos = ["♠️ Picas", "♣️ Tréboles", "♦️ Diamantes", "♥️ Corazones"]
numeros = list(range(1, 10))
mazo = [(numero, palo) for palo in palos for numero in numeros]
random.shuffle(mazo)

opciones_fichas = ["1", "2", "3", "4", "5", ">", ">>", ">>>", ">>>>", "Ω"]
st.sidebar.write("SELECCIÓN DE FICHAS:")
fichas_guardadas = st.sidebar.pills(
    "Fichas", 
    options=opciones_fichas, 
    selection_mode="multi", 
    label_visibility="collapsed"
)

if not fichas_guardadas:
    fichas_guardadas = []

num_misiones = st.sidebar.number_input("NÚMERO DE MISIONES:", min_value=1, max_value=40, step=1)
lon_fichas = len(fichas_guardadas)


if st.button("GENERAR MISIÓN", use_container_width=True, type="primary"):
    with st.spinner('Asignando misión...'):
        time.sleep(1.2)
        
    columnas = st.columns(3)
    
    for i in range(num_misiones):
        carta = mazo.pop()
        indice_col = i % 3
        
        with columnas[indice_col]:
            with st.container(border=True):
                if i < lon_fichas:
                    st.write(carta[1])
                    st.header(carta[0])
                    st.warning(f"FICHA: {fichas_guardadas[i]}")
                else:
                    st.write(carta[1])
                    st.header(carta[0])