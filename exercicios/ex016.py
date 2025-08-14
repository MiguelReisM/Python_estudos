#Crie um programa que leia um numero real qualuqer pelo teclado e mostre na tela a sua porcao inteira
import math

num1 = float(input('Digite um numero: '))
print(f'O numero {num1} tem a parte inteira {math.trunc(num1)}')