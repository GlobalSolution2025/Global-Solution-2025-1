import streamlit as st
from api_sensor.api_request.api_get_ultimo_dado import get_sensor_data_renamed

def carregar_dados():
    if 'ultimo_dado' not in st.session_state or st.session_state['atualizar']:
        st.session_state['ultimo_dado'] = get_sensor_data_renamed()
        st.session_state['atualizar'] = False
    return st.session_state['ultimo_dado']