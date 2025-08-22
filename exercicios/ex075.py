#Crie um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# quantas vezes apareceu o valor 9
# em que posicao foi digitado o primeiro valor 3
# quais foram os numeros pares
lista_num = []
for c, n in enumerate(range(4)):
    num = int(input(f'Digite o {c} valor: '))
    lista_num.append(num)