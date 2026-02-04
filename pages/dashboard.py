import streamlit as st

if not st.session_state.get("logado"):
    st.stop()

st.title("📊 Painel do Corretor")

st.page_link("pages/cadastro_imovel.py", label="➕ Cadastrar imóvel")
st.page_link("pages/vitrine.py", label="📱 Minha vitrine")
