import json
from pathlib import Path

ARQUIVO_USUARIOS = Path("data/usuarios.json")

def carregar_usuarios():
    if ARQUIVO_USUARIOS.exists():
        return json.loads(ARQUIVO_USUARIOS.read_text())
    return []

def salvar_usuarios(usuarios):
    ARQUIVO_USUARIOS.write_text(json.dumps(usuarios, indent=2))

import streamlit as st

st.title("📝 Cadastro do Corretor")

# Inicializa lista de usuários se não existir
if "usuarios" not in st.session_state:
    st.session_state.usuarios = []

nome = st.text_input("Nome completo")
email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")
creci = st.text_input("CRECI")
whatsapp = st.text_input("WhatsApp")

if st.button("Criar conta"):
    if not nome or not email or not senha:
        st.error("Preencha todos os campos obrigatórios.")
    else:
        st.session_state.usuarios.append({
            "nome": nome,
            "email": email,
            "senha": senha,
            "creci": creci,
            "whatsapp": whatsapp
        })
        st.success("Cadastro realizado com sucesso! Agora faça login.")
        st.page_link("pages/login.py", label="Ir para o login")

