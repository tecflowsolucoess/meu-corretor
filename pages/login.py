import streamlit as st
from services.auth import autenticar

st.title("🔐 Login - MEU CORRETOR")

email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    ok, tipo = autenticar(email, senha)
    if ok:
        st.session_state.logado = True
        st.session_state.usuario = email
        st.session_state.tipo = tipo
        st.switch_page("pages/dashboard.py")
    else:
        st.error("Credenciais inválidas")
