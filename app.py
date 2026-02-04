import streamlit as st

st.set_page_config(
    page_title="Meu Corretor",
    page_icon="🏡",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.usuario = None
    st.session_state.tipo = None

st.title("🏡 MEU CORRETOR")

if not st.session_state.logado:
    st.info("Faça login para continuar")
    st.page_link("pages/login.py", label="🔐 Entrar")
else:
    st.success(f"Bem-vindo, {st.session_state.usuario}")
    st.page_link("pages/dashboard.py", label="📊 Painel")
