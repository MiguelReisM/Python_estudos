#Crie um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# quantas vezes apareceu o valor 9
# em que posicao foi digitado o primeiro valor 3
# quais foram os numeros pares
lista_num = []
lista_par = []
for c, n in enumerate(range(4)):
    num = int(input(f'Digite o {c+1} valor: '))
    if num % 2 == 0:
        lista_par.append(num)
    lista_num.append(num)
print(f'Aqui esta a sua tupla: {lista_num}')
print(f'O valor 9 apreceu {lista_num.count(9)} vezes')
print(f'O valor 3 apreceu primeiro na {lista_num.index(3+1)} posicaos')
print(f'Os valores pares foram {lista_par}')