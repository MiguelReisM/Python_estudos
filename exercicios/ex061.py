#Crie um programa que leia o primeiro termo e a razao de uma PA (progressao aritmetica). No final, mostrando os 10 primeiros termos desse programa mas usando o while
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

cont = 1
termo = pt

print('\nOs 10 primeiros termos dessa PA são:')
while cont <= 10:
    print(termo, end=' ')
    termo += r
    cont += 1