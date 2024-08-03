import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.title("Mi primer sitio con streamlit")

# Generar datos de ejemplo
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=100)
data = pd.DataFrame({
    'Date': dates,
    'Value': np.random.randn(100).cumsum()
})

# Crear dos columnas
col1, col2 = st.columns([3, 1])

# Gráfico de línea en la primera columna
with col1:
    st.subheader("Gráfico de Línea")
    fig = px.line(data, x='Date', y='Value', title='Evolución del Valor')
    line_chart = st.plotly_chart(fig)

# Selector de datos y botón en la segunda columna
with col2:
    st.subheader("Controles")
    start_date = st.date_input("Fecha de inicio", value=data['Date'].min(), min_value=data['Date'].min(), max_value=data['Date'].max())
    end_date = st.date_input("Fecha de fin", value=data['Date'].max(), min_value=data['Date'].min(), max_value=data['Date'].max())
    
    if st.button("Calcular"):
        # Filtrar datos según la selección
        filtered_data = data[(data['Date'] >= pd.to_datetime(start_date)) & (data['Date'] <= pd.to_datetime(end_date))]
        
        # Actualizar el gráfico
        fig_filtered = px.line(filtered_data, x='Date', y='Value', title='Evolución del Valor (Filtrado)')
        line_chart.plotly_chart(fig_filtered)
