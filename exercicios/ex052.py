#Crie um programa que leia um numero inteiro e diga se ele é ou nao um numero primo
num = int(input("Digite um número inteiro: "))

if num <= 1:
    print(f"{num} não é um número primo.")
else:
    primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break

    if primo:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")