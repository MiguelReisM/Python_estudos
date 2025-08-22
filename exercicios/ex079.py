#Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista. Caso o numero ja exista la dentro, ele nao sera adicionado
# No final, serao exibidos todos os valores unicos digitados, em ordem crescente 
lista_numerica = []
contador = 0

while True:
    while contador == 0:
        numero = int(input('Digite um valor: '))
        lista_numerica.append(numero)
        break

    while contador > 0:
        numero = int(input('Digite um valor: '))
        existe = lista_numerica.count(numero)
        if existe > 0:
            print('Esse numero ja foi inserido, tente outro!')
        else:
            lista_numerica.append(numero)
            break

    while True:
        opcao = ''
        opcao = (input('Voce deseja continuar? (S/N): ')).strip().lower()[0]
        if 'n' in opcao: break
        elif 's' in opcao: 
            break
        else: print('Digite uma opcao valida')
    if opcao == 'n': break

    contador += 1

print('=-' * 20)
print(sorted(lista_numerica))