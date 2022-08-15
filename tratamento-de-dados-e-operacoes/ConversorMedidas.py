# Conversor de Medidas - Exercício 8

medida = float(input('Digite uma distância em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km =  medida / 1000
print(f'A distância dos metros digitados corresponde a: \n - {mm}mm, \n - {cm}cm, \n - {dm}dm, \n - {dam}dam, \n - {hm}hm, \n - {km}km.')


