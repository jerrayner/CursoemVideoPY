# Pintando Parede - Exercício 11

largura =float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m². ')
tinta = area / 2
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta.')
