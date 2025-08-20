#Crie um programa que leia o primeiro termo e a razao de uma PA (progressao aritmetica). No final, mostrando os termos desse programa mas usando o while
# Pergunte ao usuario se ele quer mostrar mais alguns termos, o programa se incerra quando ele disser qu quer mostrar 0 termos
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont_final = 1
cont_adicional = 10

cont = 1
termo = pt

print('\nOs 10 primeiros termos dessa PA são:')
while cont_final != 0:
    while cont <= 10:
        print(termo, end=' ')
        termo += r
        cont += 1
    print('\nQuer mostrar mais quantos termos? ')
    cont_final = int(input('Digite quantos termos quer: '))
    cont_adicional += cont_final
    while cont <= cont_adicional:
        print(termo, end=' ')
        termo += r
        cont += 1
