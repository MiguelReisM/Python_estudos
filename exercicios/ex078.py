#Crie um programa que leia 5 valores numericos e guarde os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posicoes na lista
lista_num = []
for numeros in range(5):
    numero = int(input(f'Digite o seu {numeros + 1}° numero: '))
    lista_num.append(numero)
print(f'A sua lista é: {lista_num}')
print(f'Sendo o maior valor {max(lista_num)} encontrado na {lista_num.index(max(lista_num))+ 1}° posicao')
print(f'Sendo o menor valor {min(lista_num)} encontrado na {lista_num.index(min(lista_num))+ 1}° posicao')
