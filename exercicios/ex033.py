#Crie um programa que leia 3 numeros e mostre qual é o maior e o menor
num1 = int(input('Digite o seu primeiro numero:'))
num2 = int(input('Digite o seu segundo numero:'))
num3 = int(input('Digite o seu terceiro numero:'))

if num1 > num2:
    if num1 > num3:
        print(f'O numero {num1} é o maior')
    else:
        print(f'O numero {num3} é o maior')
elif num2 > num3:
    print(f'O numero {num2} é o maior')
else:
    print(f'O numero {num3} é o maior')

if num1 < num2:
    if num1 < num3:
        print(f'O numero {num1} é o menor')
    else:
        print(f'O numero {num3} é o menor')
elif num2 < num3:
    print(f'O numero {num2} é o menor')
else:
    print(f'O numero {num3} é o menor')