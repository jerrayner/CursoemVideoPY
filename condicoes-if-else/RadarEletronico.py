# Radar Eletrônico - Exercício 29


velocidade = float(input('Digite a velocidade do carro: '))
multa = 7.00*(velocidade-80)
if velocidade > 80:
    print(f'O limite permitido é de 80km/h. Você foi multado!\n Você irá pagar R${multa}')
else:
    print('Boa viagem! Dirija com cuidado.')