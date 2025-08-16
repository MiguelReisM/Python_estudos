#Crie um programa que leia 3 numeros e mostre qual é o maior e o menor
num1 = int(input('Digite o seu primeiro numero:'))
num2 = int(input('Digite o seu segundo numero:'))
num3 = int(input('Digite o seu terceiro numero:'))

menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'O menor valor digitado é: {menor}')
print(f'O maior valor digitado é: {maior}')