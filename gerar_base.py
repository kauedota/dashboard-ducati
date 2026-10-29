"""Gera uma base ficticia de 100 vendas da Ducati (dado cru + sanitizado).

Uso: python gerar_base.py
Saidas: vendas_ducati.csv (cru e sanitizado) e dados.json (so sanitizado, usado no index.html).
"""
import csv
import json
import random

random.seed(911)

MODELOS = {  # modelo: (preco base em R$, peso)
    "Panigale V4": (190_000, 3), "Streetfighter V4": (170_000, 3), "Monster": (85_000, 8),
    "Multistrada V4": (160_000, 6), "Scrambler": (62_000, 7), "Diavel V4": (175_000, 2),
    "Hypermotard 950": (95_000, 3), "DesertX": (125_000, 4),
}
CIDADES = {
    "São Paulo": "SP", "Campinas": "SP", "Rio de Janeiro": "RJ", "Belo Horizonte": "MG",
    "Curitiba": "PR", "Porto Alegre": "RS", "Brasília": "DF", "Florianópolis": "SC",
}
PAGAMENTOS = ["À vista", "Financiamento", "Consórcio", "Leasing"]
ANOS = [2021, 2022, 2023, 2024, 2025]

# variantes "sujas" para simular o dado cru
SUJO_CIDADE = {
    "São Paulo": ["sao paulo", "SAO PAULO", " São Paulo "], "Campinas": ["campinas", "CAMPINAS"],
    "Rio de Janeiro": ["rio de janeiro", "RJ - Rio"], "Belo Horizonte": ["belo horizonte", "BH"],
    "Curitiba": ["curitiba", "CURITIBA "], "Porto Alegre": ["porto alegre", "POA"],
    "Brasília": ["brasilia", "BRASILIA"], "Florianópolis": ["florianopolis", "Floripa"],
}
SUJO_PAG = {
    "À vista": ["a vista", "AVISTA", "à vista "], "Financiamento": ["financiamento", "FINANC.", "financ"],
    "Consórcio": ["consorcio", "CONSORCIO"], "Leasing": ["leasing", "LEASING "],
}

linhas = []
for i in range(1, 101):
    modelo = random.choices(list(MODELOS), [v[1] for v in MODELOS.values()])[0]
    cidade = random.choices(list(CIDADES), [6, 2, 4, 3, 2, 2, 2, 1])[0]
    pag = random.choices(PAGAMENTOS, [4, 4, 1, 1])[0]
    ano = random.choices(ANOS, [1, 2, 3, 4, 5])[0]
    preco = round(MODELOS[modelo][0] * random.uniform(0.92, 1.2) / 100) * 100

    cru_preco = f"R$ {preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    if random.random() < 0.15:
        cru_preco = str(preco)
    cru_ano = str(ano) if random.random() > 0.1 else f"'{ano}"
    linhas.append({
        "id": i,
        "modelo_cru": modelo.lower() if random.random() < 0.2 else modelo,
        "cidade_cru": random.choice(SUJO_CIDADE[cidade]) if random.random() < 0.3 else cidade,
        "estado_cru": CIDADES[cidade] if random.random() > 0.1 else CIDADES[cidade].lower(),
        "ano_cru": cru_ano,
        "preco_cru": cru_preco,
        "pagamento_cru": random.choice(SUJO_PAG[pag]) if random.random() < 0.3 else pag,
        "modelo": modelo, "cidade": cidade, "estado": CIDADES[cidade],
        "ano": ano, "preco": preco, "pagamento": pag,
    })

with open("vendas_ducati.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(linhas[0]), delimiter=";")
    w.writeheader()
    w.writerows(linhas)

campos = ["id", "modelo", "cidade", "estado", "ano", "preco", "pagamento"]
with open("dados.json", "w", encoding="utf-8") as f:
    json.dump([{k: l[k] for k in campos} for l in linhas], f, ensure_ascii=False, separators=(",", ":"))

print(f"{len(linhas)} vendas | receita total R$ {sum(l['preco'] for l in linhas):,.0f}")

# embute os dados sanitizados no index.html (entre /*DADOS*/ e /*FIM*/)
import re
html = open("index.html", encoding="utf-8").read()
dados = open("dados.json", encoding="utf-8").read()
html = re.sub(r"/\*DADOS\*/.*?/\*FIM\*/", lambda m: f"/*DADOS*/{dados}/*FIM*/", html, flags=re.S)
open("index.html", "w", encoding="utf-8").write(html)
print("index.html atualizado")
