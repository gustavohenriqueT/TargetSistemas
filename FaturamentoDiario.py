import json

# Ler o arquivo JSON com os dados de faturamento diário
with open('dados.json', 'r') as file:
    dados = json.load(file)

# Inicializar variáveis
menorfaturamento = float()
maiorfaturamento = float()
somafaturamento = 0
diasacima = 0

# Ler o dados da lista
dados = {}

# Calcular menor e maior faturamento e somar os valores de faturamento para calcular a média
for faturamento in dados:
    if faturamento > maiorfaturamento:
        maiorfaturamento = faturamento
    if faturamento < menorfaturamento:
        menorfaturamento = faturamento
    somafaturamento += faturamento

# Calcular a média de faturamento, ignorando os dias sem faturamento
diascomfaturamento = len([f for f in dados if f > 0])
if diascomfaturamento > 0:
    mediafaturamento = somafaturamento / diascomfaturamento
else:
    mediafaturamento = 0

# Contar o número de dias em que o faturamento foi superior à média mensal
for faturamento in dados:
    if faturamento > mediafaturamento:
        diasacima += 1

# Imprimir os resultados
print("Menor faturamento: R$ {:.2f}".format(menorfaturamento))
print("Maior faturamento: R$ {:.2f}".format(maiorfaturamento))
print("Dias acima da média: {}".format(diasacima))