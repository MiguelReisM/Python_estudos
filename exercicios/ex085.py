#Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separdos os valores pares e impares.
# No final, mostre os valores pares e impares em ordem crescente (uma lista com 2 listas internas)
lista_valores = []
par = []
impar = []

for v in range(7):
    valor = int(input((f'Digite o {v + 1} valor: ')))
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

lista_valores = ([par, impar])

print(f'Os valores pares digitados sao: {sorted(lista_valores[0])}')
print(f'Os valores impares digitados sao {sorted(lista_valores[1])}')
