import streamlit as st
from services.usuarios_service import autenticar_usuario
from services.session_service import salvar_login, recuperar_usuario_logado

st.set_page_config(page_title="Login - Meu Corretor", layout="centered")

# Sessão base
if "logado" not in st.session_state:
    st.session_state.logado = False

if "usuario" not in st.session_state:
    st.session_state.usuario = None

# 🔁 Recuperar login automático
usuario_id = recuperar_usuario_logado()

if usuario_id and not st.session_state.logado:
    st.session_state.logado = True
    st.session_state.usuario = {"id": usuario_id}
    st.switch_page("pages/dashboard.py")

st.title("🔐 Login - Meu Corretor")

email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    usuario = autenticar_usuario(email, senha)

    if usuario:
        st.session_state.logado = True
        st.session_state.usuario = usuario
        salvar_login(usuario)
        st.success("Login realizado com sucesso!")
        st.switch_page("pages/dashboard.py")
    else:
        st.error("E-mail ou senha inválidos")

st.divider()
st.page_link("pages/cadastro.py", label="📝 Criar conta")
