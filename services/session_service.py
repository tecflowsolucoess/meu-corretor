import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

cookies = EncryptedCookieManager(
    prefix="meu_corretor_",
    password="troque_essa_senha_por_algo_seguro"
)

if not cookies.ready():
    st.stop()


def salvar_login(usuario):
    cookies["usuario_id"] = usuario["id"]
    cookies.save()


def limpar_login():
    cookies.clear()
    cookies.save()


def recuperar_usuario_logado():
    return cookies.get("usuario_id")
