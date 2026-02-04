import streamlit as st
from services.usuarios_service import criar_usuario

st.set_page_config(page_title="Cadastro - Meu Corretor", layout="centered")

st.title("📝 Cadastro do Corretor")

nome = st.text_input("Nome")
email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")

if st.button("Criar conta"):
    if not nome or not email or not senha:
        st.error("Preencha todos os campos")
    else:
        resultado = criar_usuario(email, senha, nome)

        if isinstance(resultado, dict) and "erro" in resultado:
            st.error(resultado["erro"])
        else:
            st.success("Conta criada com sucesso!")
            st.switch_page("pages/login.py")
