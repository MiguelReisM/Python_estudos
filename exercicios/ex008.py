#Crie um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
medida = float(input('Digite a metragem: '))

print(f'Foram digitados {medida:.2f}M, que são o mesmo que {medida * 100:.0f}cm e tantos milimetros {medida * 1000 :.0f}mm')