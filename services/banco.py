import json
import os
from datetime import datetime

ARQUIVO = "dados_imoveis.json"

def _carregar():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def _salvar(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def salvar_imovel(usuario, imovel):
    dados = _carregar()
    imovel["usuario"] = usuario
    imovel["criado_em"] = datetime.now().isoformat()
    dados.append(imovel)
    _salvar(dados)

def listar_imoveis(usuario):
    dados = _carregar()
    return [i for i in dados if i["usuario"] == usuario]

