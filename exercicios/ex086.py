#Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatacao correta
linha = []
coluna = []

for l in range(3):
    linha = []
    for c in range(3):
        linha.append(int(input(f'Digite um valor para {[l,c]}: ')))
    coluna.append(linha)

for l in range(3):
    for c in range(3):
        print(f'[{coluna[l][c]:^5}]', end='')
    print()