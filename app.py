# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# ---- Leer los datos ----
car_data = pd.read_csv('vehicles_us.csv')

# ---- Encabezado ----
st.header("Cuadro de Mandos: Análisis de Vehículos en Venta")
st.write("Explora datos de vehículos a la venta mediante histogramas y gráficos de dispersión interactivos.")

# ---- Botón para Histograma ----
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para la columna "odometer"')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# ---- Botón para Gráfico de Dispersión ----
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: "odometer" vs "price"')
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="model_year",  # puedes cambiar a otra columna si quieres
        hover_data=["model", "condition"]
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# ---- Opcional: Checkboxes ----
st.write("---")
st.write("Opcional: seleccionar qué gráficos mostrar")

if st.checkbox('Mostrar histograma'):
    st.write('Construyendo histograma...')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

if st.checkbox('Mostrar gráfico de dispersión'):
    st.write('Construyendo gráfico de dispersión...')
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="model_year",
        hover_data=["model", "condition"]
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
