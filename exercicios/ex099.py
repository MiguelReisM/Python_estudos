#Crie um programa que tenha uma funcao chamada maior(), que receba varias parametros com valores inteiros
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior
def maior(*valor):
    print('=-' * 20)
    print('Analisando valores...')
    print(*valor)
    print(f'Foram informados {len(valor)} valores ao todo.')

    if valor:
        maior_v = valor[0]
        for v in valor:
            if v > maior_v:
                maior_v = v
        print(f'O maior valor informado foi {maior_v}')
    else:
        print('Nao foram informados valores, nao temos o maior')


valores1 = [2, 9, 4, 5, 7, 1]
maior(*valores1)

valores2 = [4, 7, 0]
maior(*valores2)

valores3 = [1, 2]
maior(*valores3)

valores4 = [6]
maior(*valores4)

valores4 = [ ]
maior(*valores4)