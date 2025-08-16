#Crie um programa que leia um numero inteiro qualuqer e mostre se ele é PAR ou IMPAR
numero = int(input('Digite um numero:'))

if (numero % 2) == 1:
    print(f'O numero {numero} é impar!')
else:
        print(f'O numero {numero} é par!')
