# Analisando Triângulo - Exercício 35

a = float(input('Insira a primeira medida: '))
b = float(input('Insira a segunda medida: '))
c = float(input('Insira a terceira medida: '))
lista = [a, b, c]
if a + b + c - max(lista) > max(lista):
    print('Os seguimentos acima PODEM formar um triângulo.')
else:
    print('Os seguimentos acima NÃO PODEM formar um triângulo.')