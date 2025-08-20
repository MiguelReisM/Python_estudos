#Crie um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci usando while
# 0 - 1 - 1 - 2 - 3 - 5 - 8
num1 = num3 = 0
num2 = cont = 1
vezes = int(input('Digite quantos elementos da sequenci de fibonacci voce quer ver: '))

while  cont <= vezes:
    print(num3, end=' ')
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    cont += 1
    if cont == 3:
        num3 = 1
        num2 -= 1
