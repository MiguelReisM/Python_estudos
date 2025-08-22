#Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla
# Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao na tupla
from random import randint

numeros = []

for n in range(5):
    numeros.append(randint(0,10))

print(f'Números gerados: {sorted(numeros)}')
print(f'Maior número: {max(numeros)}')
print(f'Menor número: {min(numeros)}')