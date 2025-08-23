#Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separdos os valores pares e impares.
# No final, mostre os valores pares e impares em ordem crescente (uma lista com 2 listas internas)
lista_valores = [[], []]

for c in range(1,8):
    valor = int(input((f'Digite o {c} valor: ')))
    if valor % 2 == 0:
        lista_valores[0].append(valor)
    else:
        lista_valores[1].append(valor)

print(f'Os valores pares digitados sao: {sorted(lista_valores[0])}')
print(f'Os valores impares digitados sao {sorted(lista_valores[1])}')
