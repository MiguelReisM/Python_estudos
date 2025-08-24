#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um dicionario.
# No final, coloque esse dicionario em ordem sabendo que o vencedor tirou o maior numero no dado
from random import randint

resultado = {'jogador1' : randint(1,6),
            'jogador2' : randint(1,6),
            'jogador3' : randint(1,6),
            'jogador4' : randint(1,6)
            }

for k, v in resultado.items():
    print(f'O {k} tirou: {v}')

print('\nRanking dos jogadores')

ranking = sorted(resultado.items(), key=lambda x: x[1], reverse=True)

for pos, (k, v) in enumerate(ranking, start=1):
    print(f'{pos}º lugar: {k} com {v}')