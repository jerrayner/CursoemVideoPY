# Sorteando um item na lista - Exercicio 19

import random

nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')
lista = [nome1, nome2, nome2, nome4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')
