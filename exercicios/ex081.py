#Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, mostre:
# Quantos numeros foram digitados
# A lista de valores ordenado de forma decrescente
# Se o valor 5 foi digitado e esta ou nao na lista
lista_numerica = []
c = 0

while True:
    numero = int(input('Digite um numero: '))
    lista_numerica.append(numero)
    c += 1

    while True:
        opcao = ''
        opcao = (input('Voce deseja continuar? (S/N): ')).strip().lower()[0]
        if 'n' in opcao: break
        elif 's' in opcao: 
            break
        else: print('Digite uma opcao valida')
    if opcao == 'n': break

print(f'\nForam inseridos {c} numeros na lista: {sorted(lista_numerica)}')
print(f'A lista em ordem decrescente fica: {sorted(lista_numerica, reverse= True)}')
if lista_numerica.count(5) > 0:
    print('O numero 5 esta na lista!')
else:
    print('O numero 5 nao esta na lista!')