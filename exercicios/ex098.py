#Crie um programa que tenha uma funcao chamada contador, que receba tres parametros: inicio, fim, passo, e realize a contagem
# Seu programa tem que realizar tres contagens atraves da funcao criada:
# de 1 ate 10 de 1 em 1
# de 10 ate 0 de 2 em 2
# uma contagem personalizada
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        print(f'A contagem de {inicio} até {fim} de {passo} em {passo} nao existe, alterando para 1 em 1:', end=' ')
        passo = 1

    print(f'\nA contagem de {inicio} até {fim} de {passo} em {passo}:', end=' ')

    if inicio < fim:
        c = inicio
        while c <= fim:
            print(f'{c} ', end='')
            c += passo
    else:
        c = inicio
        while c >= fim:
            print(f'{c} ', end='')
            c -= passo


contador(1, 10, 1)
contador(10, 0, 2)

print(f'\n{"-=" * 20}')
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)