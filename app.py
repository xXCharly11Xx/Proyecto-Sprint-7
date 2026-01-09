import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.header('Panel de anuncios de venta de vehículos')

# Cargar los datos
df = pd.read_csv('vehicles_us.csv')

# Mostrar una muestra de los datos
st.write('Vista previa del conjunto de datos')
st.dataframe(df.head())

# Casilla para histograma
build_hist = st.checkbox('Mostrar histograma del odómetro')

if build_hist:
    st.write('Distribución del kilometraje de los vehículos')
    fig_hist = px.histogram(df, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla para gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión (precio vs odómetro)')

if build_scatter:
    st.write('Relación entre precio y kilometraje')
    fig_scatter = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)
