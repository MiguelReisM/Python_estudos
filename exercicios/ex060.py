#Crie um programa que leia um numero qualquer e mostre o fatorial
# Obs: existe um metodo para calculo de fatorial 'from math import factorial', que facilita esse codigo.
print('Veja o fatorial de um número!')
num = int(input('Digite um número: '))
resultado = 1
contador = num

while contador > 0:
    resultado *= contador
    contador -= 1

print(f'O fatorial de {num}! é = {resultado}')
