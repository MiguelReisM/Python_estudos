#Crie um programa que gerencie o aproveitamento de varios jogadores de futebol. O programa vai ler o nome dos jogadores e quantas partidas eles jogaram.
# Depois vai ler quantidade de gols feitos em cada partida. No final, tudo isso sera guardado em um dicionario, incluindo o total de gols feito durante o campeonato
# Inclua um sistema de visualizacao de detalhes do aproveitamento de cada jogador
lista_jogadores = []

while True:
    jogador = {}
    jogador['nome'] = input('Nome: ').strip().title()
    partidas = int(input('Quantas partidas ele jogou? '))

    gols = []
    for p in range(partidas):
        g = int(input(f'- Quantos gols ele fez na {p+1}ª partida? '))
        gols.append(g)

    jogador['gols'] = gols
    jogador['total'] = sum(gols)

    lista_jogadores.append(jogador)

    opcao = input('Deseja continuar? (S/N): ').strip().upper()[0]
    if opcao == 'N':
        break

print('-' * 40)
print(f'{"cod":<4}{"Nome":<12}{"Gols":<18}{"Total":<5}')
print('-' * 40)
for cod, j in enumerate(lista_jogadores):
    print(f'{cod:<4}{j["nome"]:<12}{str(j["gols"]):<18}{j["total"]:<5}')

while True:
    print('-' * 40)
    resp = input('Mostrar dados de qual jogador? (999 para parar) ').strip()
    if not resp.isdigit():
        print('Digite um código numérico válido.')
        continue

    cod = int(resp)
    if cod == 999:
        break
    if 0 <= cod < len(lista_jogadores):
        jogador = lista_jogadores[cod]
        print(f'-- Levantamento do jogador {jogador["nome"]}:')
        for i, g in enumerate(jogador['gols'], start=1):
            print(f'   No jogo {i} fez {g} gol(s).')
    else:
        print('Código inválido! Tente novamente.')
