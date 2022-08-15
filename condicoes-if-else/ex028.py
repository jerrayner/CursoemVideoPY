# Jogo de Adivinhe o Número

from random import randint

computador = randint(0, 5)
print('*' * 20)
print('Adivinhe o número entre 0 e 5.')
print('*' * 20)
jogador = int(input('Em que número eu pensei?'))
if jogador == computador:
    print('Você venceu!')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}!')