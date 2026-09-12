# Sistema de Desconto Progressivo para E-Commerce

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Instituição](https://img.shields.io/badge/Instituição-ETEC%20%7C%20CPS-B20000?style=for-the-badge)](https://www.cps.sp.gov.br/)
[![Disciplina](https://img.shields.io/badge/Disciplina-DS%20I%20--%20Agenda%2006-0969DA?style=for-the-badge)]()

<div align="center">
  <br>
  <img src="carrinhodecompras.gif" alt="Simulação Carrinho de Compras" width="120px" />
  <br>
</div>

## 📌 Sobre o projeto

Programa em Python que calcula o desconto progressivo aplicado a uma compra online, de acordo com o valor total informado pelo cliente. Atividade da **Agenda 06** da disciplina **Desenvolvimento de Sistemas I** (Curso Técnico em Desenvolvimento de Sistemas — ETEC/CPS).

## 💼 Regras de desconto

| Valor da compra (R$) | Desconto |
| --- | :---: |
| Menor que 200,00 | 5% |
| De 200,00 até 299,99 | 10% |
| A partir de 300,00 | 15% |



## 🧠 Como o código funciona

O programa segue o modelo **entrada → processamento → saída**:

1. **Entrada:** lê o valor da compra digitado pelo usuário e converte para `float`.
2. **Decisão:** uma estrutura `if / elif / else` define a taxa de desconto conforme a faixa de valor. Como o `elif` só é avaliado quando a condição anterior é falsa, não é preciso repetir o limite inferior em cada verificação (por exemplo, não é necessário escrever `valor_compra >= 200 and valor_compra < 300`, já que o `elif` só chega ali se `valor_compra < 200` já foi descartado).
3. **Processamento:** o cálculo do desconto e do valor final é feito uma única vez, fora da estrutura condicional — assim evita-se repetir a mesma fórmula em cada bloco (`if`, `elif`, `else`).
4. **Saída:** os resultados são exibidos formatados com duas casas decimais.

```python
# Processamento: cálculo feito uma única vez, fora da estrutura de decisão
valor_desconto = valor_compra * taxa_desconto
valor_final = valor_compra - valor_desconto
```

## 🧪 Casos de teste

| Valor digitado | Desconto aplicado | Valor do desconto | Total a pagar |
| :---: | :---: | :---: | :---: |
| R$ 150,00 | 5% | R$ 7,50 | R$ 142,50 |
| R$ 200,00 | 10% | R$ 20,00 | R$ 180,00 |
| R$ 299,99 | 10% | R$ 30,00 | R$ 269,99 |
| R$ 300,00 | 15% | R$ 45,00 | R$ 255,00 |
| R$ 500,00 | 15% | R$ 75,00 | R$ 425,00 |

Os valores de R$ 200,00 e R$ 300,00 são casos de fronteira: testam se o programa usa corretamente o operador `<` (estrito) nos limites das faixas.

## 🚀 Como executar

```bash
git clone https://github.com/gu1just1/etec-ds1-agenda06.git
cd etec-ds1-agenda06
python GuilhermeJusti_Ag6_DS_I.py
```

### Exemplo de saída

```text
Digite o valor total da compra (R$): 200.00
----------------------------------------
Taxa aplicada:      10%
Valor do desconto:  R$ 20.00
Total a pagar:      R$ 180.00
----------------------------------------
```

## 📂 Estrutura de arquivos

```text
etec-ds1-agenda06/
│
├── GuilhermeJusti_Ag6_DS_I.py   # Script principal
├── README.md                    # Este arquivo
└── carrinhodecompras.gif        # Gif ilustrativo
```

## 👨‍💻 Autor

**Guilherme Justi** — Curso Técnico em Desenvolvimento de Sistemas, ETEC/CPS
Disciplina: Desenvolvimento de Sistemas I — Agenda 06
