frase1 = 'Curso em Video Python'

# FATIAMENTO DE STRINGS
frase1[9:13] # imprimir do caractere 9 ao 13

# ANÁLISE DE STRINGS
frase1.len() # retorna tamanho da string
frase1.count('o') # retorna a quantidade de caracteres 'o'
frase1.find('deo') # retornará em qual posição se encontra os caracteres 'deo'
print('Curso' in frase1) # Retornará True ou False, no caso se existe a string CURSO na frase.

# TRANSFORMAÇÃO DE STRING
frase1.replace('Python', 'Android') # substituirá a string python por android
frase1.upper() # deixando tudo em maiusculas
frase1.lower() # deixando tudo em minusculas
frase1.capitalize() # String toda em minuscula, menos o primeiro caractere da String
frase1.title() # Todos os primeiros caracteres das palavras da string em maiusculas
frase1.rstrip() # remove os espaços do lado direito da string: right
frase1.lstrip() # remove os espaços do lado esquerdo: left
frase1.strip() # remove todos os espaços existentes nas extremidades da string.

# DIVISÃO DE STRINGS
frase1.split() # gera uma lista com todas as palavras da string, separando - palavra 1 curso, 2 em, 3 video, 4 python, por padrão divide-se considerando os espaços

# JUNÇÃO DE STRINGS
print('-'.join(frase)) # gera uma nova string com as palavras separadas por '-'
