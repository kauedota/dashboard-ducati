# Dashboard de Vendas Ducati

Dashboard interativa em HTML de arquivo único (Chart.js) com 100 vendas fictícias de motos Ducati no Brasil, de 2021 a 2025. Ela responde três perguntas de negócio e tem filtros e indicadores no topo.

**Dashboard publicada:** https://kauedota.github.io/dashboard-ducati/
**Repositório:** https://github.com/kauedota/dashboard-ducati

## Perguntas de negócio e por quê

1. **Quais modelos geram mais receita?** (barras) Ajuda a decidir onde concentrar estoque e marketing. O modelo líder fica destacado em vermelho.
2. **A receita cresce ano a ano?** (linha) Mostra se o negócio está em expansão ou estagnado.
3. **Como o cliente paga, e o ticket médio muda por estado?** (rosca e barras) A forma de pagamento afeta o caixa e o risco. O ticket por estado indica onde estão os clientes de maior valor. Barras mais claras sinalizam poucas vendas, ou seja, uma leitura menos confiável.

**Filtros:** modelo, estado, ano e forma de pagamento, com botão para limpar.
**Indicadores de topo:** total de vendas, receita, ticket médio e modelo líder.
Cada gráfico tem uma frase de insight que se atualiza conforme o filtro.

## Base de dados e tratamento

Não tinha a planilha da Porsche do curso, e o professor já usou essa marca. Por isso **gerei uma base fictícia da Ducati** com o script `gerar_base.py`, que usa uma semente fixa e por isso é reproduzível. Não há nenhum dado real ou pessoal.

O arquivo `vendas_ducati.csv` guarda cada campo em duas versões, como no desafio:

| Campo | Cru (exemplos) | Sanitizado |
|---|---|---|
| modelo | `monster` | `Monster` |
| cidade | `sao paulo`, `BH`, ` São Paulo ` | `São Paulo`, `Belo Horizonte` |
| estado | `sp` | `SP` |
| ano | `'2022` | `2022` (número) |
| preço | `R$ 155.100,00` | `155100` (número) |
| pagamento | `FINANC.`, `a vista` | `Financiamento`, `À vista` |

Antes de gerar a dashboard, usei só as colunas sanitizadas, com preço e ano como números e sem fórmulas (`dados.json`). Esses dados ficam embutidos no `index.html`.

## Prompt e o que mudou até a versão final

Prompt inicial (a partir do enunciado do desafio):

> Quero fazer a dashboard do desafio: um HTML de arquivo único, com 3 perguntas de negócio, filtros, indicadores de topo e visual coerente, publicado no GitHub Pages. Não tenho a planilha, pode usar dados aleatórios.

O que mudou ao longo da construção:

- **Marca:** comecei com a Porsche e troquei para a Ducati (moto), já que o professor tinha feito a Porsche.
- **Dados:** como a planilha não estava disponível, gerei a base com um script. O script também cria a versão "crua" de cada campo, para documentar o tratamento.
- **Stack:** HTML com Chart.js, escolhido por ser arquivo único e publicar direto no GitHub Pages.
- **Pergunta 3:** ficou em dois gráficos (formas de pagamento e ticket médio por estado), com aviso visual de amostra pequena.

## Ferramenta usada

Usei **Claude Code** (assistente de código no editor), sem ChatGPT Canvas e sem agente com skill. O resultado são os arquivos deste repositório, gerados e conferidos nele.

## Arquivos

- `index.html`: a dashboard, com os dados embutidos
- `vendas_ducati.csv`: base completa, crua e sanitizada
- `dados.json`: base sanitizada que vai no HTML
- `gerar_base.py`: gera a base e atualiza o `index.html`

Para regenerar a base e atualizar a dashboard: `python gerar_base.py`.
