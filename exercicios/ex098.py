#Crie um programa que tenha uma funcao chamada contador, que receba tres parametros: inicio, fim, passo, e realize a contagem
# Seu programa tem que realizar tres contagens atraves da funcao criada:
# de 1 ate 10 de 1 em 1
# de 10 ate 0 de 2 em 2
# uma contagem personalizada
def contador(inicio, fim, passo):
    if inicio < fim and passo > 0 or inicio > fim and passo < 0:
        print(f'A contagem de {inicio} até {fim} de {passo} em {passo} é: ')
        for c in range(inicio, fim + 1, passo):
            print(f'{c}', end=' ')
    elif inicio > fim and passo > 0 or inicio < fim and passo < 0:
        print(f'A contagem de {inicio} até {fim} de {passo} em {passo} é: ')
        for c in range(inicio, fim - 1, - (passo)):
            print(c, end=' ')
    elif inicio < fim and passo == 0:
        print(f'A contagem de {inicio} até {fim} de {passo} em {passo} nao existe, alterando para 1 em 1: ')
        for c in range(inicio, fim + 1, 1):
            print(c, end=' ')
    else:
        print(f'A contagem de {inicio} até {fim} de {passo} em {passo} nao existe, alterando para 1 em 1: ')
        for c in range(inicio, fim - 1, - 1):
            print(c, end=' ')
    print(f'\n{"-" * 40}')


inicio_a = 1
fim_a = 10
passo_a = 1
contador(inicio_a, fim_a, passo_a)

inicio_b = 10
fim_b = 0
passo_b = 2
contador(inicio_b, fim_b, passo_b)

inicio_c = int(input('Inicio: '))
fim_c = int(input('Fim: '))
passo_c = int(input('Passo: '))
contador(inicio_c, fim_c, passo_c)