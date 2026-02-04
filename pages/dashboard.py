if not st.session_state.get("logado"):
    st.switch_page("pages/login.py")
import streamlit as st
from services.session_service import recuperar_usuario_logado, limpar_login
from services.banco import listar_imoveis

st.set_page_config(page_title="Painel do Corretor", layout="wide")

# 🔒 Proteção
if not st.session_state.get("logado"):
    usuario_id = recuperar_usuario_logado()

    if not usuario_id:
        st.switch_page("pages/login.py")
    else:
        st.session_state.logado = True
        st.session_state.usuario = {"id": usuario_id}

st.title("📊 Painel do Corretor")

if st.button("🚪 Sair"):
    limpar_login()
    st.session_state.logado = False
    st.session_state.usuario = None
    st.rerun()

imoveis = listar_imoveis(st.session_state.usuario)

col1, col2 = st.columns(2)

with col1:
    st.metric("🏠 Imóveis cadastrados", len(imoveis))

with col2:
    st.metric("👀 Visualizações", 0)

st.divider()

st.page_link("pages/cadastro_imovel.py", label="➕ Cadastrar novo imóvel")
st.page_link("pages/vitrine.py", label="📱 Minha vitrine")
