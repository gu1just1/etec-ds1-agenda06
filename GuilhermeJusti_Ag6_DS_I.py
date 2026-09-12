# ==============================================================================
# Curso: Técnico em Desenvolvimento de Sistemas - ETEC / CPS
# Disciplina: Desenvolvimento de Sistemas I - Agenda 06
# Objetivo: Sistema de cálculo de desconto progressivo para compras online
# ==============================================================================

# Entrada de dados: leitura do valor total e conversão para float
valor_compra = float(input("Digite o valor total da compra (R$): "))

# Estrutura de decisão encadeada (if-elif-else) para definir a taxa de desconto
if valor_compra < 200.00:
    taxa_desconto = 0.05  # 5% para compras abaixo de R$ 200,00
elif valor_compra < 300.00:
    taxa_desconto = 0.10  # 10% para compras entre R$ 200,00 e R$ 299,99
else:
    taxa_desconto = 0.15  # 15% para compras a partir de R$ 300,00

# Processamento: cálculos centralizados fora da estrutura de decisão
valor_desconto = valor_compra * taxa_desconto
valor_final = valor_compra - valor_desconto

# Saída de dados: exibição dos resultados formatados com duas casas decimais
print("-" * 40)
print(f"Taxa aplicada:      {taxa_desconto * 100:.0f}%")
print(f"Valor do desconto:  R$ {valor_desconto:.2f}")
print(f"Total a pagar:      R$ {valor_final:.2f}")
print("-" * 40)