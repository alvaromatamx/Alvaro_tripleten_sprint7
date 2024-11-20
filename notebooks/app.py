import pandas as pd 
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('/Users/alvaromata/s7_vehicles_alvaro.scv')
st.header("Vehicles in the US")

histograma = st.checkbox('Construir Histograma')

if histograma:
    st.write("Creación de un histograma")

#crear el histograma 
fig = px.histogram(car_data, x="odometer")
st.plotly_chart(fig, use_container_width=True)

dispersion = st.checkbox('contruir un gráfico de dispersión')

if dispersion:
    st.write('creación de un gráfico de dispersión')

#crear gráfico de dispersión 
grafico = px.scatter(car_data, x='odometer', y='price')
st.plotly_chart(grafico, use_container_width=True)




