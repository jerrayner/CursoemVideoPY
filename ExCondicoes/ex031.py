# Custo de Viagem

km = float(input('Qual a distância em (Km) você deseja percorrer? '))
if km <= 200:
    print(f'Sua passagem vai custar R${km *0.5}')
else:
    print(f'Sua passagem vai custar R${km *0.45}')