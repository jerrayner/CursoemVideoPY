# Reajuste Salarial
'''Faça um algoritmo que leia o salário de um funcionário
e mostre o novo salário, com 15% de aumento.'''


salario = float(input('Qual o salário do funcionário? R$'))
reajuste = salario + (salario * 15 / 100)

print(f'O funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${reajuste}.')
