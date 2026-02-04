import streamlit as st

st.title("🔐 Login - MEU CORRETOR")

email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")

if st.button("Entrar"):
    usuarios = st.session_state.get("usuarios", [])

    usuario = next(
        (u for u in usuarios if u["email"] == email and u["senha"] == senha),
        None
    )

    if usuario:
        st.session_state.logado = True
        st.session_state.usuario = usuario["nome"]
        st.success("Login realizado com sucesso!")
        st.page_link("pages/dashboard.py", label="Ir para o painel")
    else:
        st.error("E-mail ou senha inválidos")

st.divider()
st.page_link("pages/cadastro.py", label="📝 Criar conta")
