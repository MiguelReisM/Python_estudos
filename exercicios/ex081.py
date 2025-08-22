#Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, mostre:
# Quantos numeros foram digitados
# A lista de valores ordenado de forma decrescente
# Se o valor 5 foi digitado e esta ou nao na lista
lista_numerica = []
lista_par = []
lista_impar = []
c = 0

while True:
    numero = int(input('Digite um numero: '))
    lista_numerica.append(numero)
    c += 1

    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

    while True:
        opcao = ''
        opcao = (input('Voce deseja continuar? (S/N): ')).strip().lower()[0]
        if 'n' in opcao: break
        elif 's' in opcao: 
            break
        else: print('Digite uma opcao valida')
    if opcao == 'n': break

print(f'\nForam inseridos {c} numeros na lista: {sorted(lista_numerica)}')
print(f'Sendo esses os pares {sorted(lista_par)}')
print(f'E esses os impares {sorted(lista_impar)}')