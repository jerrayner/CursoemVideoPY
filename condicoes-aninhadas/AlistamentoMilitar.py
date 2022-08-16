# Alistamento Militar - Exercício 39

from datetime import date

atual = date.today().year
nome = str(input('Digite seu nome: '))
sexo = str(input('Sexo Feminino(F) ou Masculino(M): '))
anoNasc = int(input('Ano de Nascimento: '))
if sexo == 'f' or sexo == 'F':
    print('Seu alistamento não é obrigatório.')
    continua =  str(input('Deseja continuar? (SIM) | (NÃO) - '))
    if continua == 'NÃO' or continua == 'não' or continua == 'nao' or continua == 'NAO':
        print('Obrigado!')
idade = atual - anoNasc
anosRestantes = (18 - idade) + 2022  # calculo do ano em que deverá comparecer ao alistamento
anoAli = 2022 - (idade - 18)
if idade == 18:
    print(f'Você tem {idade} anos, precisa se alistar até o dia 30 de junho deste ano.')
elif idade < 18:
    print(f'Você tem {idade} anos, faltam {18-idade} ano(s) para seu alistamento, você deverá se alistar em {anosRestantes}. ')
elif idade > 18:
    print(f'Seu alistamento foi {idade-18} anos atrás, foi no ano de {anoAli}. Se você for mulher e tiver menos que 29 anos, ainda poderá comparecer e solicitar alistamento.')
print('Obrigado!')



