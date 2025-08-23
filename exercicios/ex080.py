#Crie um programa onde o ususario possa digitar cinco valores numericos e cadastre-os em uma lista, ja na posicao correta de insercao (sem usar o sort())
# No final, mostre a lista ordenada na tela
lista_num = []

for n in range(5):
    numero = int(input('Digite um numero: '))
    if n == 0 or numero > lista_num[-1]:
        lista_num.append(numero)
        print(f'O número {numero} foi adicionado ao final da lista!')
    else:
        posicao = 0
        while posicao < len(lista_num):
            if numero <= lista_num[posicao]:
                lista_num.insert(posicao, numero)
                print(f'O número {numero} foi adicionado na {posicao + 1}° posição da lista!')
                break
            posicao += 1

print(lista_num)