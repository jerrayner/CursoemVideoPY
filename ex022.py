# Analisador de Textos

nome = (input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome completo em maiusculas é {nome.upper()}')
print(f'Seu nome completo em minusculas é {nome.lower()}')
espacos = (nome.count(' '))
print(f'Seu nome tem ao todo {len(nome) - espacos} letras')
primeiro = nome.find(' ')
print(f'Seu primeiro nome tem {primeiro} letras.')
'''

Nessa parte do código surgiu um erro que não consegui resolve-lo.
print(f'Seu nome tem ao todo {nome.len()} letras') # o erro estava em colocar nome.len, quando a variavel deveria vir antes de len
lista = nome.split()
print(f'Seu primeiro nome é {lista[0]}, e ele tem {len(lista[0])} letras')'''


