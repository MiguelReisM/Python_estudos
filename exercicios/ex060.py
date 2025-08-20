#Crie um programa que leia um numero qualquer e mostre o fatorial
print('Veja o fatorial de um numero!')
num1 = int(input('Digite um numero: '))
num2 = num1 - 1
resultado = 1

while num2 > 0:
    resultado *= (num1 * num2)
    num1 -= 2
    num2 -= 2
print(f'O fatorial desse numero é {resultado}')

#Obs: existe um metodo para calculo de fatorial 'from math import factorial', que facilita esse codigo.