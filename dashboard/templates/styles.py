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