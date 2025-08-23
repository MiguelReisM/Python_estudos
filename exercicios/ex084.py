#Crie um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre: (<= 70 leve // >= 100 Pesado )
# Quantas pessoas foram cadastradas
# Uma listagem com as pessoas mais pesadas e o maior peso
# Uma listagem com as pessoas mais leves e o menor peso
pessoas = []
cont = 1

while True:
    nome = input(f'Digite o nome da {cont}ª pessoa: ').strip().title()
    peso = float(input(f'Digite o peso da {cont}ª pessoa em (Kg): '))
    pessoas.append([nome, peso])

    opcao = input('\nVoce deseja continuar? (S/N): ').strip().lower()
    if opcao == 'n':
        break
    elif opcao != 's':
        print("Opcao invalida, continuando cadastro...")

    cont += 1

maior_peso = menor_peso = pessoas[0][1]
n_maior_peso = [pessoas[0][0]]
n_menor_peso = [pessoas[0][0]]

for nome, peso in pessoas[1:]:
    if peso > maior_peso:
        maior_peso = peso
        n_maior_peso = [nome]
    elif peso == maior_peso:
        n_maior_peso.append(nome)

    if peso < menor_peso:
        menor_peso = peso
        n_menor_peso = [nome]
    elif peso == menor_peso:
        n_menor_peso.append(nome)

print(f'\nForam inseridas {len(pessoas)} pessoas na lista.')
print(f'O maior peso foi de {maior_peso}Kg.\nNome de pessoas condideradas pesadas:  {n_maior_peso}')
print(f'O menor peso foi de {menor_peso}Kg.\nNome de pessoas condideradas leves:  {n_menor_peso}')