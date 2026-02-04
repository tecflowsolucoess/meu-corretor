import streamlit as st

if not st.session_state.get("logado"):
    st.warning("Você precisa estar logado para acessar esta página.")
    st.stop()
