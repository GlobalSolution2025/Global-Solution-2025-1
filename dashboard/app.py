# app.py

import streamlit as st
import json
from dashboard.templates.widgets import create_gauge, fire_status_widget
from dashboard.templates.styles import set_custom_styles
from dashboard.utils.data_handler import carregar_dados
from ml.src.models.train_model import predicao

def app():
    # Configurações iniciais
    st.set_page_config(page_title="Fire Monitoring", layout="wide")
    set_custom_styles()

    # Título
    st.markdown('<div class="title">🔥 Fire Monitoring</div>', unsafe_allow_html=True)

    # Colunas iniciais
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="block">Alerta de eventos/ocorrência</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="block">Dados dos eventos/ocorrências</div>', unsafe_allow_html=True)

    # Atualização manual
    if st.sidebar.button("🔄 Atualizar dados"):
        st.session_state['atualizar'] = True
    else:
        st.session_state['atualizar'] = st.session_state.get('atualizar', False)

    # Carregar os dados mais recentes
    ultimo_dado = carregar_dados()
    if ultimo_dado:
        st.markdown(
            "<div style='display: flex; justify-content: center;'>"
            "<table style='border-collapse: collapse;'><tr><th style='padding: 8px; border: 1px solid #ddd;'>Chave</th><th style='padding: 8px; border: 1px solid #ddd;'>Valor</th></tr>"
            + "".join(
            f"<tr><td style='padding: 8px; border: 1px solid #ddd;'>{k}</td><td style='padding: 8px; border: 1px solid #ddd;'>{v}</td></tr>"
            for k, v in ultimo_dado.items()
            )
            + "</table></div>",
            unsafe_allow_html=True
        )

    # Previsão de status de fogo
    status_fogo = int(predicao(json.dumps(ultimo_dado)))

    # Widget de status de fogo
    fire_status_widget(status_fogo)

    # Dashboard
    st.markdown('<div class="dashboard">', unsafe_allow_html=True)
    st.subheader("Dashboard - Qualidade do ar")

    # Conversão dos dados
    temperatura = int(ultimo_dado.get('temperatura_superficie', 0))
    umidade = int(ultimo_dado.get('umidade_relativa', 0))
    nivel_gas = int(ultimo_dado.get('concentracao_CO2', 0))

    # Gauges
    col3, col4, col5 = st.columns(3)
    with col3:
        st.plotly_chart(create_gauge(temperatura, "Temperatura", "orange"), use_container_width=True)
        st.markdown(f"<div style='text-align: center;'><strong>Temperatura: {temperatura}°C</strong></div>", unsafe_allow_html=True)
    with col4:
        st.plotly_chart(create_gauge(umidade, "Umidade", "blue"), use_container_width=True)
        st.markdown(f"<div style='text-align: center;'><strong>Umidade: {umidade}%</strong></div>", unsafe_allow_html=True)
    with col5:
        st.plotly_chart(create_gauge(nivel_gas, "Nível de gás/fumaça", "green"), use_container_width=True)
        st.markdown(f"<div style='text-align: center;'><strong>Nível de gás: {nivel_gas} ppm</strong></div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
