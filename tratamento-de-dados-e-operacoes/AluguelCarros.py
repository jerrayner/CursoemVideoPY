# Aluguel de Carros - Exercicio 15

km_rodado = int(input('Quantos km o carro rodou? '))
dias_alugados = int(input('Quantos dias o carro permaneceu alugado? '))
custo_km = float(input(f'Qual o custo do km rodado? R$ '))
custo_dia = float(input(f'Qual é o custo do carro por dia? R$ '))

print(f'O custo dos {km_rodado} Kms rodados é R$ {km_rodado * custo_km:.2f} ')
print(f'O custo de {dias_alugados} dias do carro é R$ {dias_alugados * custo_dia:.2f}')
print(f'O custo total do aluguél do carro ficou em : R$ {(km_rodado * custo_km) + (dias_alugados * custo_dia):.2f}')