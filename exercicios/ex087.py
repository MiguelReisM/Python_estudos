#Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatacao correta, junto a:
# A soma de todos os valores pares
# A soma dos valores da terceira coluna
# O maior valor da segunda linha
linha = []
coluna = []
soma_c3 = soma_par = 0

for l in range(3):
    linha = []
    for c in range(3):
        linha.append(int(input(f'Digite um valor para {[l,c]}: ')))
    coluna.append(linha)

for l in range(3):
    for c in range(3):
        print(f'[{coluna[l][c]:^5}]', end='')
        if coluna[l][c] % 2 == 0:
            soma_par += coluna[l][c]
    print()

for l in range(3): #somatorio da coluna 3
    soma_c3 += coluna[l][2]

for c in range(3): #maior valor da linha 2
    if c == 0:
        maior = coluna[1][c]
    else:
        if coluna[1][c] > maior:
            maior = coluna[1][c]

print('-=' * 20)
print(f'A soma de todos os valores pares é: {soma_par}')
print(f'A soma dos valores da terceira coluna é: {soma_c3}')
print(f'O maior valor da segunda linha é: {maior}')