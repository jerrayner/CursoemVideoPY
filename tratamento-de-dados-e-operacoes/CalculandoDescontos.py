# Calculando Descontos - Exercício 12

valor = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o desconto: '))
valorDescontado = float(valor * desconto / 100)
valorFinal = float(valor - valorDescontado)
print(f'O produto com valor de R${valor}, na promoção com desconto de {desconto}% vai custar {valorFinal}')
