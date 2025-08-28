#Crie um programa que tenha uma funcao cahamada ficha(), que receba dois parametros: o nome de um jogador e quantos gols ele marcou.
# O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente
def ficha(nome='', gols=''):

    if nome.strip() == '':
        nome = 'desconhecido'
    if str(gols).isnumeric():
        gols = int(gols)
    else:
        gols = 0

    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


n = input('Digite o nome do jogador: ').strip().title()
g = input('Digite quantos gols ele fez: ')
print(ficha(n, g))