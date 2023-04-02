# Dados de cada estado
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Declaração das variáveis para calcular
valor_total = sum(faturamento_estados.values())

# Calculo completo do Percentual de cada Estado
for estado, faturamento in faturamento_estados.items():
    percentual = faturamento / valor_total * 100
    print(f'{estado}: {percentual:.2f}%')
