#Crie um programa que ajude um jogador da Mega Sena a criar palpites.
# O programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
from random import randint

jogo = []

print('-=' * 15)
print(f'{'Jogo da Mega Sena':^30}')
print('-=' * 15)

jogos = int(input('Quantos jogos voce quer que eu sorteie? '))

for j in range(jogos):
    jogo = []
    for pos in range(6):
        while True:
            num = randint(1, 60)
            if pos == 1 or num not in jogo:
                jogo.append(num)
                break

    print(f'Jogo {j + 1}: {sorted(jogo)}')
