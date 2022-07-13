# Conversor de Moedas

valor = float(input('Digite um valor em reais: '))
dolar = valor / 5.20
euro = valor / 5.20
libra = valor / 6.40
peso = valor / 0.042
print(f'Com R${valor} você pode comprar DS${dolar:.2f}.')
print(f'Em euros, com o valor de R${valor}, você poderá ter ${euro:.2f}')
print(f'Em libras, com o valor de R${valor}, você poderá ter £{libra:.2f}')
print(f'Em pesos, com o valor de R${valor}, você poderá ter Mex${peso:.2f}')



