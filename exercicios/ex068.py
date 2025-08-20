#Crie um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador Perder, mostre o total de vitorias consecutivas que ele conquistou no final do jogo
from random import randint

vitorias = 0

print('=-'*12)
print(' Jogando Par ou Ímpar!')
print('=-'*12)

while True:
    num_c = randint(0, 9)

    num_j = int(input('\nDigite um número: '))
    opcao = int(input('Escolha: 1 - PAR | 2 - ÍMPAR: '))

    if opcao not in (1, 2):
        print('\nDigite uma opção válida!')
        continue

    soma = num_c + num_j
    resultado = 'PAR' if soma % 2 == 0 else 'ÍMPAR'

    print(f'Você jogou {num_j}, o computador {num_c}. Total = {soma} → {resultado}')

    ganhou = (opcao == 1 and resultado == 'PAR') or (opcao == 2 and resultado == 'ÍMPAR')

    if ganhou:
        vitorias += 1
        print('Você ganhou!')
    else:
        print('Você perdeu!')
        break

print(f'\nFim de jogo, você fez {vitorias} vitória(s) seguida(s)!')