#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler quantidade de gols feitos em cada partida. No final, tudo isso sera guardado em um dicionario, incluindo o total de gols feito durante o campeonato
somatoria = 0
gol_partida = []
jogador = {}

jogador['nome'] = input('Nome: ').strip().title()
jogador['partidas'] = int(input('Quantas partidas ele jogou? '))

for p in range(jogador['partidas']):
    partida = int(input(f'Quantos gols ele fez na {p+1}ª partida: '))
    gol_partida.append(partida)
    somatoria += partida

jogador['gols'] = gol_partida[:]
jogador['total'] = somatoria

print(f'\nO jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for c in range(jogador['partidas']):
    print(f' => Na partida {c+1}, fez {gol_partida[c]} gol(s)')
print(f'Foi um total de {jogador["total"]} gol(s)')
