import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Fire Monitoring", layout="wide")

# Função para criar o gauge
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

# Estilos
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
        .icon {
            font-size: 30px;
            margin-right: 10px;
        }
        .dashboard {
            border: 2px solid #4DA6FF;
            border-radius: 10px;
            padding: 20px;
            background-color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown('<div class="title">🔥 Fire Monitoring</div>', unsafe_allow_html=True)

# Primeira linha: Alertas e Dados
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="block">**Alerta de eventos/ocorrência**</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="block">**Dados dos eventos/ocorrências**</div>', unsafe_allow_html=True)

# Dashboard: qualidade do ar
st.markdown('<div class="dashboard">', unsafe_allow_html=True)
st.subheader("Dashboard - Qualidade do ar")

# Simulação de valores
temperatura = st.slider("Temperatura", 0, 100, 25)
umidade = st.slider("Umidade", 0, 100, 40)
nivel_gas = st.slider("Nível de gás/fumaça", 0, 100, 10)

col3, col4, col5 = st.columns(3)

with col3:
    st.plotly_chart(create_gauge(temperatura, "Temperatura", "orange"), use_container_width=True)

with col4:
    st.plotly_chart(create_gauge(umidade, "Umidade", "blue"), use_container_width=True)

with col5:
    st.plotly_chart(create_gauge(nivel_gas, "Nível de gás/fumaça", "green"), use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)
