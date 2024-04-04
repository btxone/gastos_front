import streamlit as st
import requests
import logging

# Configurar el logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

st.title('Registro de Gastos')

# Nuevo campo para el nombre del archivo Excel
excel_name = st.text_input('Nombre del archivo Excel (sin la extensión .xlsx)')

price = st.number_input('Precio', format="%f")
description = st.text_input('Descripción')

if st.button('Enviar'):
    try:
        response = requests.post('http://54.234.42.22:8000/add-expense', json={'price': price, 'description': description, 'excel_name': excel_name})
        if response.status_code == 200:
            st.success('Gasto registrado con éxito.')
            logger.info(f"Gasto registrado: {price} - {description} en {excel_name}.xlsx")
        else:
            st.error('Hubo un problema al registrar el gasto.')
            logger.error(f"Error al registrar gasto: {response.status_code} - {response.text}")
    except Exception as e:
        st.error('No se pudo conectar al servidor para registrar el gasto.')
        logger.exception("Excepción al conectar con el servidor: ", exc_info=e)
