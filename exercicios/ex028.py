#Crie um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5 e peca para o usuario tentar descobri qual foi o numero escolhido pelo computador.
# O programa deverá escrever na tela se o usuario acertou ou errou.
import random

numero_u = int(input('Digite um numero de 0 a 5: '))
opcoes = [0,1,2,3,4,5]
numero_c = random.choice(opcoes)

if 0 < numero_u <= 6:
    if numero_u == numero_c:
        print(f'Voce acertou! O numero era {numero_c}')
    else:
        print(f'Infelizmente voce errou... O numero era {numero_c}')
else:
    print('Digite um numero valido')