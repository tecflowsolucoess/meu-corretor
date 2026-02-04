import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="Vitrine de Imóveis", layout="wide")

# =========================
# ARQUIVOS
# =========================
ARQUIVO_IMOVEIS = Path("data/imoveis.json")

def carregar_imoveis():
    if ARQUIVO_IMOVEIS.exists():
        return json.loads(ARQUIVO_IMOVEIS.read_text())
    return []

# =========================
# PEGA O CORRETOR DA URL
# =========================
params = st.query_params
email_corretor = params.get("corretor")

if not email_corretor:
    st.warning("Vitrine não encontrada.")
    st.stop()

# =========================
# CARREGA IMÓVEIS DO CORRETOR
# =========================
imoveis = carregar_imoveis()
imoveis_corretor = [
    i for i in imoveis if i.get("corretor") == email_corretor
]

# =========================
# TOPO DA VITRINE
# =========================
st.markdown(
    """
    <style>
    .card {
        border: 1px solid #eee;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .preco {
        color: #1f7ae0;
        font-size: 22px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🏡 Vitrine de Imóveis")

if not imoveis_corretor:
    st.info("Nenhum imóvel disponível no momento.")
    st.stop()

# =========================
# LISTAGEM
# =========================
for imovel in imoveis_corretor:
    st.markdown(
        f"""
        <div class="card">
            <h3>{imovel['titulo']}</h3>
            <p><strong>Tipo:</strong> {imovel['tipo']}</p>
            <p><strong>Cidade:</strong> {imovel['cidade']}</p>
            <p class="preco">R$ {imovel['valor']:,.2f}</p>
            <p>{imovel['descricao']}</p>
            <a href="https://wa.me/?text=Tenho interesse no imóvel: {imovel['titulo']}" target="_blank">
                💬 Falar no WhatsApp
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )


