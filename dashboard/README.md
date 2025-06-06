### ✅ **Estrutura de Pastas Sugerida**

```
dashboard/
├── main.py
├── templates/
│   ├── widgets.py
│   └── styles.py
├── utils/
│   └── data_handler.py
├── api_sensor/
│   └── api_request/
│       └── api_get_ultimo_dado.py
├── ml/
│   └── src/
│       └── models/
│           └── train_model.py
```

---

### 🔁 **1. `main.py` – Ponto de Entrada**

```python
import streamlit as st
import json
from templates.widgets import create_gauge, fire_status_widget
from templates.styles import set_custom_styles
from utils.data_handler import carregar_dados

# Configurações iniciais
st.set_page_config(page_title="Fire Monitoring", layout="wide")
set_custom_styles()

# Título
st.markdown('<div class="title">🔥 Fire Monitoring</div>', unsafe_allow_html=True)

# Colunas iniciais
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="block">**Alerta de eventos/ocorrência**</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="block">**Dados dos eventos/ocorrências**</div>', unsafe_allow_html=True)

# Atualização manual
if st.sidebar.button("🔄 Atualizar dados"):
    st.session_state['atualizar'] = True
else:
    st.session_state['atualizar'] = st.session_state.get('atualizar', False)

# Carregar os dados mais recentes
ultimo_dado = carregar_dados()
if ultimo_dado:
    st.sidebar.markdown(f"**Último dado recebido:** {ultimo_dado}")

# Previsão de status de fogo
from ml.src.models.train_model import predicao
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
with col4:
    st.plotly_chart(create_gauge(umidade, "Umidade", "blue"), use_container_width=True)
with col5:
    st.plotly_chart(create_gauge(nivel_gas, "Nível de gás/fumaça", "green"), use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)
```

---

### 🧩 **2. `templates/widgets.py`**

```python
import streamlit as st
import plotly.graph_objects as go

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

def fire_status_widget(value):
    color = "#FF4136" if value == 1 else "#2ECC40"
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
```

---

### 🎨 **3. `templates/styles.py`**

```python
import streamlit as st

def set_custom_styles():
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
```

---

### 🔄 **4. `utils/data_handler.py`**

```python
import streamlit as st
from api_sensor.api_request.api_get_ultimo_dado import get_sensor_data_renamed

def carregar_dados():
    if 'ultimo_dado' not in st.session_state or st.session_state['atualizar']:
        st.session_state['ultimo_dado'] = get_sensor_data_renamed()
        st.session_state['atualizar'] = False
    return st.session_state['ultimo_dado']
```

---

Com isso, você pode rodar o app com:

```bash
streamlit run main.py
```
