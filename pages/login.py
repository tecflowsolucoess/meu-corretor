import streamlit as st

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
        st.switch_page("pages/dashboard.py")
    else:
        st.error("E-mail ou senha inválidos")


st.divider()
st.page_link("pages/cadastro.py", label="📝 Criar conta")
