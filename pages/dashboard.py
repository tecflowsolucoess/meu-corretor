import streamlit as st
from services.banco import listar_imoveis

# =========================
# PROTEÇÃO DE LOGIN
# =========================
if not st.session_state.get("logado"):
    st.warning("Você precisa estar logado para acessar esta página.")
    st.stop()

st.set_page_config(page_title="Painel do Corretor", layout="wide")

# =========================
# DADOS DO USUÁRIO
# =========================
usuario = st.session_state.usuario
email = usuario["email"]

# =========================
# LINK DA VITRINE (TOPO)
# =========================
link_vitrine = f"https://meu-corretor.streamlit.app/?corretor={email}"

st.markdown("### 🔗 Link da sua vitrine pública")
st.code(link_vitrine, language="text")

st.divider()

# =========================
# TÍTULO
# =========================
st.title("📊 Painel do Corretor")

# =========================
# DADOS
# =========================
imoveis = listar_imoveis(email)

col1, col2 = st.columns(2)

with col1:
    st.metric("🏠 Imóveis cadastrados", len(imoveis))

with col2:
    st.metric("👀 Visualizações", 0)

st.divider()

# =========================
# AÇÕES
# =========================
st.page_link("pages/cadastro_imovel.py", label="➕ Cadastrar novo imóvel")
st.page_link("pages/vitrine.py", label="📱 Ver minha vitrine")

st.divider()

# =========================
# LOGOUT
# =========================
if st.button("🚪 Sair"):
    st.session_state.clear()
    st.switch_page("pages/login.py")
