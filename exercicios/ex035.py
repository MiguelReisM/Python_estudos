#Crie um programa que leia o comprimento de 3 retas e diga ao ususario se elas podem ou nao formar um triangulo
reta1 = int(input('Digite o valor da primeira reta: '))
reta2 = int(input('Digite o valor da segunda reta: '))
reta3 = int(input('Digite o valor da terceira reta: '))

if reta1 + reta2 > reta3:
    if reta1 + reta3 > reta2:
        if reta2 + reta3 > reta1:
            print('É possivel formar um triangulo!')
        else:
            print('Nao é possivel formar um triangulo')
    else:
        print('Nao é possivel formar um triangulo')
else:
    print('Nao é possivel formar um triangulo')