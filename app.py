import streamlit as st
import pandas as pd
st.title("Bolsa de Valores Quito BI")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Gabriela Flores")

archivo = st.file_uploader("Cargue su archivo")
tabla = pd.read:csv(archivo)
st.write(tabla)
