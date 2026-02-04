import streamlit as st

st.title("🔐 Login - MEU CORRETOR")

# Se já estiver logado, manda direto pro dashboard
if st.session_state.get("logado"):
    st.switch_page("pages/dashboard.py")

email = st.text_input("E-mail", key="login_email")
senha = st.text_input("Senha", type="password", key="login_senha")

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
        st.rerun()
    else:
        st.error("E-mail ou senha inválidos")

st.divider()
st.page_link("pages/cadastro.py", label="📝 Criar conta")
