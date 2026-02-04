import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="Vitrine de Imóveis", layout="wide")

# =========================
# ARQUIVO
# =========================
ARQUIVO_IMOVEIS = Path("data/imoveis.json")

def carregar_imoveis():
    if ARQUIVO_IMOVEIS.exists():
        return json.loads(ARQUIVO_IMOVEIS.read_text())
    return []

# =========================
# CORRETOR VIA URL
# =========================
params = st.query_params
email_corretor = params.get("corretor")

if not email_corretor:
    st.error("Vitrine não encontrada.")
    st.stop()

# =========================
# CARREGA IMÓVEIS
# =========================
imoveis = carregar_imoveis()
imoveis = [i for i in imoveis if i.get("corretor") == email_corretor]

# =========================
# ESTILO
# =========================
st.markdown(
    """
    <style>
    body {
        background-color: #f7f7f7;
    }
    .card {
        background: white;
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 20px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    }
    .titulo {
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 6px;
    }
    .cidade {
        color: #666;
        font-size: 14px;
        margin-bottom: 10px;
    }
    .preco {
        font-size: 24px;
        font-weight: bold;
        color: #0d6efd;
        margin-bottom: 12px;
    }
    .tipo {
        display: inline-block;
        background: #eef4ff;
        color: #0d6efd;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        margin-bottom: 10px;
    }
    .btn {
        display: block;
        text-align: center;
        background: #25d366;
        color: white;
        padding: 12px;
        border-radius: 10px;
        text-decoration: none;
        font-weight: 600;
        margin-top: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# CABEÇALHO
# =========================
st.markdown("## 🏡 Imóveis disponíveis")

if not imoveis:
    st.info("Nenhum imóvel disponível no momento.")
    st.stop()

# =========================
# GRID RESPONSIVO
# =========================
colunas = st.columns(2)

for idx, imovel in enumerate(imoveis):
    with colunas[idx % 2]:
        st.markdown(
            f"""
            <div class="card">
                <div class="tipo">{imovel['tipo']}</div>
                <div class="titulo">{imovel['titulo']}</div>
                <div class="cidade">{imovel['cidade']}</div>
                <div class="preco">R$ {imovel['valor']:,.2f}</div>
                <div>{imovel['descricao']}</div>
                <a class="btn" href="https://wa.me/?text=Tenho interesse no imóvel: {imovel['titulo']}" target="_blank">
                    💬 Falar no WhatsApp
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
