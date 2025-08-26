import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Vehículos - Dashboard", layout="wide")
st.header("Cuadro de mandos: Anuncios de coches")

@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

try:
    df = load_data()
    st.write("Vista rápida del dataset (primeras filas):")
    st.write(df.head())

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if not numeric_cols:
        st.warning("No se encontraron columnas numéricas en el dataset.")
    else:
        default_index = numeric_cols.index("price") if "price" in numeric_cols else 0
        col = st.selectbox("Elige columna numérica para el histograma:", numeric_cols, index=default_index)
        bins = st.slider("Número de bins", 10, 100, 50)

        if st.button("Construir histograma"):
            fig = px.histogram(df, x=col, nbins=bins, title=f"Histograma de {col}")
            st.plotly_chart(fig, use_container_width=True)

except FileNotFoundError:
    st.error("No se encontró 'vehicles_us.csv' junto a app.py.")
