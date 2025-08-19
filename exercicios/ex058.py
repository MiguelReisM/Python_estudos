#Crie um programa que faca o computador "pensar" em um numero inteiro entre 0 e 10 e peca para o usuario tentar descobri qual foi o numero escolhido pelo computador.
# Só que o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer
from random import randint

tentativa = 0
num_c = 0
num_h = 1

while num_c != num_h:
    num_c = randint(0, 10)
    num_h = int(input('Digite um numero entre 0 e 10: '))
    tentativa += 1
    print(f'O computador jogou {num_c} e voce jogou {num_h}')
    if num_c != num_h:
        print('Voce perdeu, proxima tentativa')
print(f'Parabens voce ganhou e usou {tentativa} tentativas')