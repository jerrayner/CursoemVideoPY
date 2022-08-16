# Primeiro e Último Nome de uma Pessoa - Exercicio 27

nome = str(input('Digite seu nome completo: ')).strip().split()

print(f"""
O seu primeiro nome é {nome[0].title()}.
O seu último nome é {nome[-1].title()}.
""")