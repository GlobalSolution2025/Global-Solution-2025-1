# main.py

from dashboard.app import app

<<<<<<< HEAD
# Configuração da página
st.set_page_config(page_title="Fire Monitoring", layout="wide")

# Função para criar gauge
def create_gauge(value, title, color):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={
            'axis': {'range': [0, 1000 if title == "Nível de gás/fumaça" else 100]},
            'bar': {'color': color},
            'bgcolor': "#f0f0f0"
        }
    ))
    fig.update_layout(margin=dict(t=20, b=20, l=20, r=20), height=200)
    return fig

# Função para exibir o status de fogo com cor e emoji 🔥
def fire_status_widget(value):
    # Se value == 1 -> vermelho, se 0 -> verde
    color = "#FF4136" if value == 1 else "#2ECC40"  # vermelho ou verde
    emoji = "🔥"
    html_content = f"""
    <div style="
        display: flex;
        align-items: center;
        font-size: 24px;
        font-weight: bold;
        color: {color};
        background-color: #222;
        padding: 10px 20px;
        border-radius: 8px;
        width: fit-content;
        margin-bottom: 20px;
        ">
        {emoji}
        <span style="margin-left: 10px;">Status do Fogo: {'ALERTA' if value == 1 else 'NORMAL'}</span>
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)

# Estilos customizados
st.markdown("""
    <style>
        .main { background-color: #f0f0f0; }
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

# Linha inicial: alertas e dados
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="block">**Alerta de eventos/ocorrência**</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="block">**Dados dos eventos/ocorrências**</div>', unsafe_allow_html=True)

# Botão de atualização manual
if st.sidebar.button("🔄 Atualizar dados"):
    st.session_state['atualizar'] = True
else:
    st.session_state['atualizar'] = st.session_state.get('atualizar', False)

# Leitura dos dados mais recentes (somente se botão for clicado ou primeira execução)
if 'ultimo_dado' not in st.session_state or st.session_state['atualizar']:
    st.session_state['ultimo_dado'] = get_sensor_data_renamed()
    st.session_state['atualizar'] = False

ultimo_dado = st.session_state['ultimo_dado']

# Exibição na barra lateral
if ultimo_dado:
    st.sidebar.markdown(f"**Último dado recebido:** {ultimo_dado}")

# Exemplo: suponha que o status do fogo seja recebido na chave 'status_fogo' (0 ou 1)
status_fogo = int(predicao(json.dumps(ultimo_dado)))

# Mostrar widget de status de fogo com cor e emoji
fire_status_widget(status_fogo)

# Dashboard
st.markdown('<div class="dashboard">', unsafe_allow_html=True)
st.subheader("Dashboard - Qualidade do ar")

# Conversão dos dados
temperatura = int(ultimo_dado.get('temperatura_superficie', 0))
umidade = int(ultimo_dado.get('umidade_relativa', 0))
nivel_gas = int(ultimo_dado.get('concentracao_CO2', 0))



# Exibição dos gauges com chaves únicas
col3, col4, col5 = st.columns(3)
with col3:
    st.plotly_chart(create_gauge(temperatura, "Temperatura", "orange"), use_container_width=True, key="gauge_temp")
    st.subheader("Temperatura")
with col4:
    st.plotly_chart(create_gauge(umidade, "Umidade", "blue"), use_container_width=True, key="gauge_umid")
    st.subheader("Umidade")
with col5:
    st.plotly_chart(create_gauge(nivel_gas, "Nível de gás/fumaça", "green"), use_container_width=True, key="gauge_gas")
    st.subheader("Nível de gás/fumaça")

st.markdown('</div>', unsafe_allow_html=True)
=======
if __name__ == "__main__":
    app()
>>>>>>> bd52d2f6d90462585b63e219e8170c777c40a087

# streamlit run main.py
