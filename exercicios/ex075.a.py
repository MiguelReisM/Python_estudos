#Crie um programa que leia quatro valores pelo teclado e guarde-os em uma lista. No final mostre:
# quantas vezes apareceu o valor 9
# em que posicao foi digitado o primeiro valor 3
# quais foram os numeros pares
lista_num = []
lista_par = []
pares = 0

for n in range(4):
    numeros = int(input(f'Digite seu numero o {n+1} numero: '))
    lista_num.append(numeros)
    if numeros % 2 == 0:
        pares += 1
        lista_par.append(numeros)

print(lista_num)

if lista_num.count(9) != 0:
    print(f'- O numero 9 aparece {lista_num.count(9)} vez(es)')
else:
    print('- O numero 9 nao aparece')

if lista_num.count(3) != 0 and lista_num.count(3) >= 2:
    print(f'- O numero 3 aparece primeiro na {lista_num.index(3) + 1} posicao')
elif lista_num.count(3) != 0 and lista_num.count(3) == 1:
    print(f'- O numero 3 apareceu na {lista_num.index(3) + 1} posicao')
else:
    print('- O numero 3 nao aprece')

if pares >= 1:
    print(f'- Esse(es) foram os numeros pares: {lista_par}')
else:
    print('- Nao temos numeros pares')

print()