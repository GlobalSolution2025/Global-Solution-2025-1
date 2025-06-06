import streamlit as st
import plotly.graph_objects as go
import time
from api_sensor.api_request.api_get_ultimo_dado import get_sensor_data_renamed

# Configuração da página
st.set_page_config(page_title="Fire Monitoring", layout="wide")

# Intervalo de atualização
refresh_interval = st.sidebar.number_input("⏱️ Intervalo de atualização (segundos)", min_value=5, max_value=300, value=10)

# Último dado do sensor
ultimo_dado = get_sensor_data_renamed()
if ultimo_dado:
    st.sidebar.markdown(f"**Último dado recebido:** {ultimo_dado}")

# Função para criar os gauges
def create_gauge(value, title, color):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': color},
            'bgcolor': "#f0f0f0"
        }
    ))
    fig.update_layout(
        margin=dict(t=20, b=20, l=20, r=20),
        height=200
    )
    return fig

# Estilos personalizados
st.markdown("""
    <style>
        .main {
            background-color: #f0f0f0;
        }
        .block {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
        }
        .title {
            font-size: 28px;
            font-weight: bold;
            color: #E4572E;
            display: flex;
            align-items: center;
        }
        .dashboard {
            border: 2px solid #4DA6FF;
            border-radius: 10px;
            padding: 20px;
            background-color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<div class="title">🔥 Fire Monitoring</div>', unsafe_allow_html=True)

# Linha de alertas e dados
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="block">**Alerta de eventos/ocorrência**</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="block">**Dados dos eventos/ocorrências**</div>', unsafe_allow_html=True)

# Dashboard
st.markdown('<div class="dashboard">', unsafe_allow_html=True)
st.subheader("Dashboard - Qualidade do ar")

# Leitura dos dados
temperatura = st.slider("Temperatura", 0, 100, ultimo_dado.get('temperatura_superficie', 0))
umidade = st.slider("Umidade", 0, 100, ultimo_dado.get('umidade_relativa', 0))
nivel_gas = st.slider("Nível de gás/fumaça", 0, 1000, ultimo_dado.get('concentracao_CO2', 0))

# Exibição dos gauges
col3, col4, col5 = st.columns(3)
with col3:
    st.plotly_chart(create_gauge(temperatura, "Temperatura", "orange"), use_container_width=True)
with col4:
    st.plotly_chart(create_gauge(umidade, "Umidade", "blue"), use_container_width=True)
with col5:
    st.plotly_chart(create_gauge(nivel_gas, "Nível de gás/fumaça", "green"), use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# Atualização automática
if 'last_refresh' not in st.session_state:
    st.session_state['last_refresh'] = time.time()

if time.time() - st.session_state['last_refresh'] > refresh_interval:
    st.session_state['last_refresh'] = time.time()
    st.experimental_rerun()
