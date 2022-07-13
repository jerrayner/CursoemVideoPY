# Verificando as Primeiras Letras de um Texto
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

nome = str(input('Onde você nasceu?: '))
org = nome.title().split()
verificador = org.count("Santo")
print(f'{bool(verificador)}')
