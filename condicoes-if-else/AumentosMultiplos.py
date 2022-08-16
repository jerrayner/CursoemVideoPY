# Aumentos Múltiplos - Exercício 34

sal = int(input('Qual é o salário do funcionário? '))
alto = sal + (sal/ 100 * 10)
if sal >= 1250:
    print(f'Quem ganhava R${sal:.2f} passa a ganhar R${alto:.2f} ')
else:
    print(f'Quem ganhava R${sal} passa a ganhar R${sal/100 * 15 + sal:.2f}')