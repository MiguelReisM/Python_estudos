#Crie um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso lidos.
menor = 0
maior = 0

for p in range(1, 6):
    peso = float(input((f'Por gentileza a {p}° pessoa informe seu peso:')))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print(f'O menor peso foi {menor}Kg e o maior {maior}Kg')
