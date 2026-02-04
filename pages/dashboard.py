import streamlit as st

if not st.session_state.get("logado"):
    st.warning("Você precisa estar logado")
    st.stop()

import streamlit as st

if not st.session_state.get("logado"):
    st.warning("Você precisa estar logado para acessar esta página.")
    st.stop()

import streamlit as st
from services.banco import listar_imoveis

if not st.session_state.get("logado"):
    st.stop()

st.title("📊 Painel do Corretor")

imoveis = listar_imoveis(st.session_state.usuario)

col1, col2 = st.columns(2)

with col1:
    st.metric("🏠 Imóveis cadastrados", len(imoveis))

with col2:
    st.metric("👀 Visualizações", 0)

st.divider()

st.page_link("pages/cadastro_imovel.py", label="➕ Cadastrar novo imóvel")
st.page_link("pages/vitrine.py", label="📱 Minha vitrine")
