# Dissecando uma variavel - Exercicio 4

something = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(something))
print('Só tem espaços? ', something.isspace())
print('É um numero? ', something.isnumeric())
print('É alfabético? ', something.isalpha())
print('Está escrito em letras maisculas? ', something.isupper())
print('Está escrito em letras minusculas?', something.islower())
print('Esta capitalizado?', something.istitle())

