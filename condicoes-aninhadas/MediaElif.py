# Média - Exercício 40

nome = str(input('Nome do aluno: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7.0 and media < 10: # maior que 7.0 e menor que 10
    print(f'O aluno {nome} teve a média de {media:.2f} e está APROVADO.')
elif media < 5.0 and media > 1.0: # menor que 5.0 e maior que 1.0
    print(f'O aluno {nome} teve a média de {media:.2f} e está REPROVADO.')
elif media > 5.0 and media < 6.9: # maior que 5.0 e menor que 6.9
    print(f'O aluno {nome} teve a média de {media:.2f} e terá que fazer a prova de RECUPERAÇÃO.')
elif media > 10.0 and media < 1.0: # para que não se digite nota maior que 10 e menor que 1.0, impossibilitando entrada de valores negativos.
    print(f'Nota inválida.')
else:
    print(f'Nota inválida.')

