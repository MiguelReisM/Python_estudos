#Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista. Caso o numero ja exista la dentro, ele nao sera adicionado
# No final, serao exibidos todos os valores unicos digitados, em ordem crescente.
lista_numerica = []
contador = 0

while True:
    while True:
        numero = int(input('Digite um valor: '))
        if numero not in (lista_numerica):
            lista_numerica.append(numero)
            break
        else:
            print('Esse valor ja esta na lista, digite outro!')

    while True:
        opcao = ''
        opcao = (input('Voce deseja continuar? (S/N): ')).strip().lower()[0]
        if opcao in 'sn': break
        else: print('Digite uma opcao valida')

    if opcao == 'n': break

print('=-' * 20)
print(sorted(lista_numerica))