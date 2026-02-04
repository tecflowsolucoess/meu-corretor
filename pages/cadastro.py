import streamlit as st
import json
from pathlib import Path

ARQUIVO_USUARIOS = Path("data/usuarios.json")

def carregar_usuarios():
    if ARQUIVO_USUARIOS.exists():
        return json.loads(ARQUIVO_USUARIOS.read_text())
    return []

def salvar_usuarios(usuarios):
    ARQUIVO_USUARIOS.parent.mkdir(exist_ok=True)
    ARQUIVO_USUARIOS.write_text(json.dumps(usuarios, indent=2))

st.title("📝 Cadastro do Corretor")

nome = st.text_input("Nome completo")
email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")
creci = st.text_input("CRECI")
whatsapp = st.text_input("WhatsApp")

if st.button("Criar conta"):
    usuarios = carregar_usuarios()

    if not nome or not email or not senha:
        st.error("Preencha todos os campos obrigatórios.")
    elif any(u["email"] == email for u in usuarios):
        st.error("Este e-mail já está cadastrado.")
    else:
        usuarios.append({
            "nome": nome,
            "email": email,
            "senha": senha,
            "creci": creci,
            "whatsapp": whatsapp
        })

        salvar_usuarios(usuarios)

        st.success("Conta criada com sucesso!")
        st.page_link("pages/login.py", label="👉 Ir para login")
