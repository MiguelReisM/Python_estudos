#Crie um programa que leia o primeiro termo e a razao de uma PA (progressao aritmetica). No final, mostrando os termos desse programa mas usando o while
# Pergunte ao usuario se ele quer mostrar mais alguns termos, o programa se incerra quando ele disser qu quer mostrar 0 termos
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

termo = pt
cont = 1
total = 0
mais = 10  # começa mostrando 10 termos

while mais != 0:
    total += mais
    while cont <= total:
        print(termo, end=' ')
        termo += r
        cont += 1
    print('\n')
    mais = int(input('Quer mostrar mais quantos termos? (0 para encerrar) '))

print(f'\nProgressão finalizada com {total} termos mostrados.')
