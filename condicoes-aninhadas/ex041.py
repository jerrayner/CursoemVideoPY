# Classificando Atletas

from datetime import date
atual = date.today().year
ano = int(input('Ano de Nascimento: '))
idade = atual - ano
print(f'O atleta tem {idade} anos de idade')
if idade <= 9:
    print('Categoria MIRIM.')

elif idade > 9 and idade < 15:
    print('Categoria INFANTIL.')

elif idade > 14 and idade < 20:
    print('Categoria JUNIOR.')

elif idade > 19 and idade < 26:
    print('Categoria é a SÊNIOR.')

else:
    print('Sua categoria é a MASTER.')