import streamlit as st
from services.banco import salvar_imovel

if not st.session_state.get("logado"):
    st.warning("Faça login para acessar")
    st.stop()

st.title("🏠 Cadastro de Imóvel")
st.caption("Cadastre seus imóveis no MEU CORRETOR")

with st.form("form_imovel"):
    titulo = st.text_input("Título do imóvel")
    tipo = st.selectbox("Tipo", ["Casa", "Apartamento", "Terreno", "Comercial"])
    preco = st.text_input("Preço (ex: R$ 350.000)")
    endereco = st.text_input("Endereço completo")
    bairro = st.text_input("Bairro")
    descricao = st.text_area("Descrição do imóvel")

    submit = st.form_submit_button("💾 Salvar imóvel")

if submit:
    if not titulo or not preco or not endereco:
        st.error("Preencha os campos obrigatórios")
    else:
        imovel = {
            "titulo": titulo,
            "tipo": tipo,
            "preco": preco,
            "endereco": endereco,
            "bairro": bairro,
            "descricao": descricao
        }

        salvar_imovel(st.session_state.usuario, imovel)
        st.success("Imóvel cadastrado com sucesso!")
