#Crie um programa que leia 5 valores numericos e guarde os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posicoes na lista
lista_num = []

for numeros in range(5):
    num = int(input(f'Digite o seu {numeros + 1}° numero: '))
    lista_num.append(num)

print(f'A sua lista é: {lista_num}')

maior = max(lista_num)
menor = min(lista_num)

print(f'\nO maior valor dessa lista é: {maior}, que aparece na(as) posicao(oes): ', end='')
for c, n in enumerate(lista_num):
    if n == maior:
        print(f'{c + 1}', end=' ')

print(f'\nO menor valor dessa lista é: {menor}, que aparece na(as) posicao(oes): ', end='')
for c, n in enumerate(lista_num):
    if n == menor:
        print(f'{c + 1}', end=' ')