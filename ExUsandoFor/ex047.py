# Contagem de Pares

from itertools import count
from time import sleep


print('Você sabe quais são os números pares do intervalo de 1 e 50?')
sleep(2)
print('Vou te mostrar!')
sleep(1)

for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=" ")
contador = int(input('Você gostaria de saber a quantidade de números pares desse intervalo?\n [1]Sim [2]Não'))
if contador == 1:
    print(count)
else:
    print('Até logo!')
