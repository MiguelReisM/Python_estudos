#Crie um programa que leia um angulo qualquer e mostre na tela o valor do seno cosseno e tangente desse angulo
import math

angulo = int(input('Digite o angulo: '))
rad = math.radians(angulo)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print(f'No angulo {angulo}° temos: \nSeno: {seno}\nCosseno: {cosseno} \nTangente: {tangente}')