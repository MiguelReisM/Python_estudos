#Crie um programa que leia um numero inteiro e diga se ele é ou nao um numero primo
num = int(input("Digite um número inteiro: "))
cont = 0

for n in range(1, num + 1):
    if num % n == 0:
        print(f'\033[32m',end=' ')
        cont += 1
    else:
        print(f'\033[31m',end=' ')
    print(f'{n}',end='')

if cont == 2:
    print(f'\n\033[mO numero {num} é primo!')
else:
    print(f'\n\033[mO numero {num} nao é primo!')