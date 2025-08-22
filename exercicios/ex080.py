#Crie um programa onde o ususario possa digitar cinco valores numericos e cadastre-os em uma lista, ja na posicao correta de insercao (sem usar o sort())
# No final, mostre a lista ordenada na tela
lista_num = []
maior = menor = 0
for n in range(5):
    numero = int(input('Digite um numero: '))
    if n == 0:
        lista_num.insert(0, numero)
        print(f'Primeiro numero adicionado a lista com sucesso!')
        maior = numero
        menor = numero
    elif n == 1:
        if numero > maior:
            lista_num.append(numero)
            maior = numero
        elif numero < menor:
            lista_num.insert(0, numero)
            menor = numero
        else:
            lista_num.append(numero)
    elif n == 2:
        if numero > maior:
            lista_num.append(numero)
        elif numero < menor:
            lista_num.insert(0, numero)
        else:
            i = lista_num.index(numero)
            lista_num.insert(i, numero)
    elif n == 3:
        if numero > maior:
            lista_num.append(numero)
        elif numero < menor:
            lista_num.insert(0, numero)
        else:
            i = lista_num.index(numero)
            lista_num.insert(i, numero)
    else:
        if numero > maior:
            lista_num.append(numero)
        elif numero < menor:
            lista_num.insert(0, numero)
        else:
            i = lista_num.index(numero)
            lista_num.insert(i, numero)

print(lista_num)