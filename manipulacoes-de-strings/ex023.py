# Separando Digitos de um Número

num = input('Digite um número entre 0 e 9999: ')
# Formata a string com 4 espaços, alinhado à direita e completa com 0
num = '{:0>4}'.format(num)

print('Unidades: {}'.format(num[3]))
print('Dezenas:  {}'.format(num[2]))
print('Centenas: {}'.format(num[1]))
print('Milhares: {}'.format(num[0]))