# 📋 Relatório de Auditoria Técnica

> **Artefato:** `GuilhermeJusti_Ag6_DS_I.py`  
> **Revisor:** Auditor de Código (Engenheiro Sênior)  
> **Ambiente de Execução:** Python 3.14.7 · Windows 11  
> **Data da Auditoria:** 2026-09-12  
> **Escopo:** Conformidade com Agenda 06 ETEC · Qualidade de Código · Trade-offs de Engenharia

---

## 1. 🎯 Resultado Executivo

| Categoria de Avaliação | Resultado | Nota |
| :--- | :---: | :---: |
| Conformidade com Requisitos da Agenda 06 | ✅ **APROVADO** | 10 / 10 |
| Aplicação do Princípio DRY | ✅ **APROVADO** | 10 / 10 |
| Otimização de Fluxo Condicional | ✅ **APROVADO** | 10 / 10 |
| Separação de Responsabilidades (SoC) | ✅ **APROVADO** | 10 / 10 |
| Cobertura de Casos de Fronteira | ✅ **APROVADO** | 10 / 10 |
| Formatação e Saída de Dados | ✅ **APROVADO** | 10 / 10 |
| Tipagem Monetária (Contexto Didático) | ⚠️ **ADEQUADO*** | 8 / 10 |

> `*` A nota 8/10 não é uma não-conformidade com a Agenda 06 — reflete apenas o trade-off entre o uso didático de `float` e a precisão exigida em produção financeira. Ver Seção 4.

**Nota Final: 9,7 / 10 — Aprovado com Distinção**

---

## 2. ✅ Validação de Conformidade com a Agenda 06 ETEC

### 2.1 Requisito: Implementação das Três Faixas de Desconto

A Agenda 06 exige a implementação de um sistema de desconto progressivo com **três faixas** determinadas pela comparação do valor da compra:

| Requisito da Agenda 06 | Implementado em `GuilhermeJusti_Ag6_DS_I.py` | Status |
| :--- | :--- | :---: |
| 5% para compras abaixo de R$ 200,00 | `if valor_compra < 200.00: taxa_desconto = 0.05` (L11–L12) | ✅ |
| 10% para compras de R$ 200,00 a R$ 299,99 | `elif valor_compra < 300.00: taxa_desconto = 0.10` (L13–L14) | ✅ |
| 15% para compras a partir de R$ 300,00 | `else: taxa_desconto = 0.15` (L15–L16) | ✅ |
| Exibir taxa aplicada | `print(f"Taxa aplicada: ...")` (L24) | ✅ |
| Exibir valor do desconto | `print(f"Valor do desconto: ...")` (L25) | ✅ |
| Exibir total a pagar | `print(f"Total a pagar: ...")` (L26) | ✅ |

**Veredicto: 100% de conformidade com os requisitos funcionais da Agenda 06.**

### 2.2 Validação das Condições de Fronteira (Inclusão/Exclusão)

A correta semântica do operador menor estrito (`<`) é crítica para a determinação inequívoca de faixa em valores exatamente iguais aos limiares:

| Valor de Fronteira | Condição Avaliada | Resultado Esperado | Resultado Obtido | Status |
| :---: | :--- | :--- | :--- | :---: |
| R$ 199,99 | `199.99 < 200.00` → `True` | Faixa 5% (L12) | 5% ✅ | ✅ |
| **R$ 200,00** | `200.00 < 200.00` → **`False`** | Faixa 10% (L14) | 10% ✅ | ✅ |
| R$ 299,99 | `299.99 < 300.00` → `True` | Faixa 10% (L14) | 10% ✅ | ✅ |
| **R$ 300,00** | `300.00 < 300.00` → **`False`** | Faixa 15% (`else`) | 15% ✅ | ✅ |

> [!IMPORTANT]
> Os pontos R$ 200,00 e R$ 300,00 são os valores de maior risco de *Off-by-One Error*. A implementação utiliza o operador `<` (menor estrito) corretamente, excluindo os limiares da faixa inferior e incluindo-os na faixa superior. **Nenhum desvio detectado.**

---

## 3. 🏗️ Análise de Complexidade e Princípio DRY

### 3.1 Mapeamento Estrutural do Artefato

```
GuilhermeJusti_Ag6_DS_I.py (27 linhas)
├── [L01–L05]  Bloco de Metadados (comentários de cabeçalho)
├── [L07–L08]  Estágio de Entrada   → captura e conversão de tipo
├── [L10–L16]  Estágio de Decisão   → determinação exclusiva de `taxa_desconto`
├── [L18–L20]  Estágio de Processamento → cálculos aritméticos centralizados
└── [L22–L27]  Estágio de Saída     → renderização formatada dos resultados
```

### 3.2 Aplicação do Princípio DRY

O princípio **DRY (*Don't Repeat Yourself*)** está rigorosamente aplicado. A estrutura `if-elif-else` opera como **atribuidor puro de estado**: sua única responsabilidade é determinar o valor de `taxa_desconto`. Nenhuma instrução aritmética ou de saída foi duplicada dentro de seus blocos.

**Implementação Auditada (L10–L20):**

```python
# Decisão: responsabilidade ÚNICA de atribuir a taxa
if valor_compra < 200.00:
    taxa_desconto = 0.05
elif valor_compra < 300.00:
    taxa_desconto = 0.10
else:
    taxa_desconto = 0.15

# Processamento: declarado UMA ÚNICA VEZ — DRY aplicado
valor_desconto = valor_compra * taxa_desconto
valor_final = valor_compra - valor_desconto
```

**Comparação com Implementação Ingênua (Antipadrão WET):**

```python
# ❌ ANTIPADRÃO — violação de DRY (NÃO está no código auditado)
if valor_compra < 200.00:
    valor_desconto = valor_compra * 0.05          # duplicado
    valor_final = valor_compra - valor_desconto   # duplicado
    print(f"Desconto: R$ {valor_desconto:.2f}")   # duplicado
elif valor_compra < 300.00:
    valor_desconto = valor_compra * 0.10          # duplicado
    valor_final = valor_compra - valor_desconto   # duplicado
    print(f"Desconto: R$ {valor_desconto:.2f}")   # duplicado
else:
    ...
```

| Métrica | Implementação Auditada | Antipadrão WET |
| :--- | :---: | :---: |
| Linhas de lógica aritmética | **2** | 6 |
| Instâncias de `print` de resultado | **3** | 9 |
| Pontos de manutenção para alterar uma fórmula | **1** | 3 |
| Complexidade Ciclomática (McCabe) | **4** | 4 |
| Risco de divergência em manutenção | **Nulo** | Alto |

**Veredicto: DRY aplicado com excelência. Redução de ~67% nos pontos de manutenção em relação à abordagem ingênua.**

### 3.3 Eliminação de Redundâncias Lógicas no Encadeamento Condicional

O interpretador Python avalia um `if-elif-else` de forma **sequencial e com curto-circuito**:

- Ao alcançar `elif valor_compra < 300.00:`, o runtime **já provou** que `valor_compra < 200.00` é `False`, o que implica `valor_compra >= 200.00`.
- A verificação `elif valor_compra >= 200.00 and valor_compra < 300.00:` seria **logicamente equivalente, porém redundante**, gerando uma instrução `LOAD_FAST` e `COMPARE_OP` desnecessária no bytecode.

**Veredicto: Sem redundâncias lógicas detectadas no encadeamento `if-elif-else`.**

---

## 4. ⚖️ Trade-offs de Engenharia: `float` Didático vs. Precisão Monetária

### 4.1 O Problema de Representação do IEEE 754

O tipo `float` do Python segue o padrão IEEE 754 de ponto flutuante de dupla precisão (64 bits). A representação binária não consegue codificar exatamente a maioria das frações decimais finitas. **Evidência coletada durante a auditoria:**

```python
# Comportamento verificado em Python 3.14.7
>>> 0.1 + 0.2
0.30000000000000004              # ← erro de representação binária

>>> 299.99 * 0.10
29.999000000000002               # ← arredondamento indesejado
```

### 4.2 Tabela Comparativa: Contexto Didático vs. Produção Financeira

| Critério | `float` (implementação atual) | `decimal.Decimal` | Inteiros em Centavos |
| :--- | :--- | :--- | :--- |
| **Precisão Decimal** | ⚠️ Aprox. 15–17 dígitos sig. | ✅ Arbitrária e configurável | ✅ Exata (sem ponto flutuante) |
| **Conformidade BACEN/FEBRABAN** | ❌ Não recomendado | ✅ Padrão de mercado | ✅ Padrão de alto desempenho |
| **Legibilidade Didática** | ✅ Alta (intuitivo) | ⚠️ Média (verboso) | ⚠️ Baixa (requer conversão na UI) |
| **Performance (operações/seg)** | ✅ ~10× mais rápido | ⚠️ Mais lento | ✅ Máxima (aritmética inteira) |
| **Risco de Acúmulo de Erro** | ⚠️ Presente em séries longas | ✅ Nulo | ✅ Nulo |
| **Adequação ao Contexto (Agenda 06)** | ✅ **Totalmente adequado** | Superdimensionado | Superdimensionado |

### 4.3 Exemplo de Implementação com `decimal.Decimal` (para referência)

```python
# Versão de produção financeira — NÃO requerida pela Agenda 06
from decimal import Decimal, ROUND_HALF_UP

valor_compra = Decimal(input("Digite o valor total da compra (R$): "))

if valor_compra < Decimal("200.00"):
    taxa_desconto = Decimal("0.05")
elif valor_compra < Decimal("300.00"):
    taxa_desconto = Decimal("0.10")
else:
    taxa_desconto = Decimal("0.15")

valor_desconto = (valor_compra * taxa_desconto).quantize(
    Decimal("0.01"), rounding=ROUND_HALF_UP
)
valor_final = valor_compra - valor_desconto
```

### 4.4 Veredicto do Trade-off

> [!NOTE]
> O uso de `float` é **totalmente adequado e correto** para o contexto pedagógico da Agenda 06 ETEC. A introdução de `decimal.Decimal` ou aritmética em centavos adicionaria complexidade conceitual desnecessária para os objetivos da disciplina de Desenvolvimento de Sistemas I. A pontuação de 8/10 nesta categoria registra formalmente o gap em relação a padrões de produção financeira — informação relevante para a evolução profissional do desenvolvedor.

---

## 5. 🧪 Cobertura de Testes — Resultados de Execução Verificados

Todos os casos foram executados com a **lógica exata do artefato auditado** em Python 3.14.7.

### 5.1 Tabela de Cobertura de Testes

| ID | Entrada (R$) | Classe de Equivalência | Taxa Aplicada | Desconto (R$) | Total a Pagar (R$) | Status |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| **TC-01** | `150.00` | Partição Inferior (P1: `v < 200`) | 5% | 7,50 | 142,50 | ✅ PASS |
| **TC-02** | `199.99` | Limite Superior de P1 | 5% | 10,00* | 189,99 | ✅ PASS |
| **TC-03** | `200.00` | **Fronteira Crítica 1** (P1→P2) | 10% | 20,00 | 180,00 | ✅ PASS |
| **TC-04** | `299.99` | Limite Superior de P2 | 10% | 30,00* | 269,99 | ✅ PASS |
| **TC-05** | `300.00` | **Fronteira Crítica 2** (P2→P3) | 15% | 45,00 | 255,00 | ✅ PASS |
| **TC-06** | `500.00` | Partição Superior (P3: `v >= 300`) | 15% | 75,00 | 425,00 | ✅ PASS |

> `*` Valor bruto do float apresenta resíduo binário (`9.9995` e `29.999...`), corrigido automaticamente pelo especificador `:.2f` na saída formatada.

### 5.2 Indicadores de Cobertura

| Métrica | Valor |
| :--- | :---: |
| Partições de Equivalência cobertas | 3 de 3 (100%) |
| Valores de Fronteira testados | 2 de 2 (100%) |
| Casos de Teste Executados | 6 |
| Casos Aprovados (`PASS`) | 6 |
| Taxa de Sucesso | **100%** |

---

## 6. 🔍 Apontamentos de Qualidade e Boas Práticas

### 6.1 Pontos Positivos (Forças do Código)

- **Comentários técnicos precisos:** Cada seção lógica é delimitada por comentários que articulam a intenção do bloco.
- **Nomenclatura semântica em português:** `valor_compra`, `taxa_desconto`, `valor_desconto`, `valor_final` comunicam domínio de negócio com clareza.
- **Separação formal de estágios:** Fluxo Input → Decision → Processing → Output explícito e rastreável.
- **Formatação de saída consistente:** Uso de `"-" * 40` para delimitadores e alinhamento visual por espaços fixos.

### 6.2 Recomendações para Evolução Profissional (fora do escopo da Agenda 06)

| Recomendação | Prioridade | Contexto de Aplicação |
| :--- | :---: | :--- |
| Substituir `float` por `Decimal` com `ROUND_HALF_UP` | Alta | Sistemas financeiros de produção |
| Adicionar validação de entrada (`try/except ValueError`) | Média | Robustez e UX em produção |
| Encapsular lógica em função `calcular_desconto(valor)` | Média | Testabilidade unitária e reutilização |
| Adicionar testes automatizados com `pytest` | Alta | Qualidade contínua em CI/CD |
| Considerar `match/case` (Python 3.10+) para faixas | Baixa | Legibilidade em cenários mais complexos |

---

## 7. 📌 Conclusão Final da Auditoria

O artefato `GuilhermeJusti_Ag6_DS_I.py` demonstra **excelência técnica no contexto pedagógico da Agenda 06 ETEC**, atendendo integralmente a todos os requisitos funcionais estabelecidos. A implementação evidencia compreensão sólida dos princípios de:

- **Estrutura de Controle de Fluxo** — uso correto e otimizado de `if-elif-else`;
- **DRY (*Don't Repeat Yourself*)** — separação exemplar entre tomada de decisão e processamento;
- **Clean Code** — nomenclatura semântica, comentários técnicos e separação de responsabilidades;
- **Análise de Casos de Fronteira** — condições de limiar implementadas sem *Off-by-One Errors*.

O único ponto de observação — o uso de `float` em vez de `Decimal` — é uma escolha pedagogicamente justificada e não representa falha ou inconformidade com os objetivos da disciplina.

---

<div align="center">
  <sub>Relatório gerado pela auditoria técnica do projeto · Desenvolvimento de Sistemas I — Agenda 06 · ETEC / CPS · 2026</sub>
</div>
