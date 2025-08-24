#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler quantidade de gols feitos em cada partida. No final, tudo isso sera guardado em um dicionario, incluindo o total de gols feito durante o campeonato
somatoria = 0
gol_partida = []
jogador = {'nome' : '',
           'partidas' : 0,
           'gols' : [],
           'total' : 0
           }

jogador['nome'] = input('Nome: ').strip().title()
jogador['partidas'] = int(input('Quantas partidas ele jogou? '))
for p in range(jogador['partidas']):
    partida = int(input(f'Quantos gols ele fez na {p} partida: '))
    gol_partida.append(partida)
    somatoria += partida
jogador['gols'] = gol_partida[:]
jogador['total'] = somatoria

print(jogador)
