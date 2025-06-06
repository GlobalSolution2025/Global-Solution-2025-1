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
