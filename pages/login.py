import streamlit as st
import json
from pathlib import Path

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Login - Meu Corretor", layout="wide")

ARQUIVO_USUARIOS = Path("data/usuarios.json")

# =========================
# FUNÇÕES
# =========================
def carregar_usuarios():
    if ARQUIVO_USUARIOS.exists():
        return json.loads(ARQUIVO_USUARIOS.read_text())
    return []

# =========================
# CONTROLE DE LOGIN
# =========================
if "logado" not in st.session_state:
    st.session_state.logado = False

if "usuario" not in st.session_state:
    st.session_state.usuario = None

# Se já estiver logado, manda direto pro dashboard
if st.session_state.logado:
    st.switch_page("pages/dashboard.py")

# =========================
# TELA
# =========================
st.title("🔐 Login - MEU CORRETOR")

email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    usuarios = carregar_usuarios()

    usuario = next(
        (
            u for u in usuarios
            if u["email"] == email and u["senha"] == senha
        ),
        None
    )

    if usuario:
        st.session_state.logado = True
        st.session_state.usuario = usuario
        st.success("Login realizado com sucesso!")
        st.switch_page("pages/dashboard.py")
    else:
        st.error("E-mail ou senha inválidos")

st.divider()

st.page_link("pages/cadastro.py", label="📝 Criar conta")
