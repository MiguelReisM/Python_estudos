#Crie um programa que leia nome sexo e idade de varias pessoas, guardadno os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista
# No final, mostre:
# Quantidade de pessoas que foram cadastradas
# A media de idade do grupo
# Uma lista com todas as mulheres
# Uma lista com todas as pessoas com a idade acima da media (30+)
pessoa = {}
lista_cadastro = []
mulheres = []
acim_med = []
idade_g = 0

while True:
    pessoa['nome'] = input('Nome: ').strip().title()
    pessoa['sexo'] = input('Sexo (M/F): ').strip().upper()

    while not sexo or sexo[0] not in 'MF':
        sexo = input('Sexo inválido. Digite M ou F: ').strip().upper()
    pessoa['sexo'] = sexo[0]

    pessoa['idade'] = int(input('Idade: '))
    idade_g += pessoa['idade']

    lista_cadastro.append(pessoa.copy())

    opcao = input('Deseja continuar? (S/N): ').upper()[0]
    if opcao == 'N': break

print('-' * 30)
print(f'Foram cadastradas {len(lista_cadastro)} pessoas')
print(f'A média de idade do grupo é: {idade_g / len(lista_cadastro):.2f} anos')

for d in lista_cadastro:
    if d['sexo'] == 'F':
        mulheres.append(d['nome'])
    if d['idade'] >= 30:
        acim_med.append(d['nome'])

if mulheres:
    print('Lista de mulheres cadastradas: ',end='')
    for nome in mulheres:
        print(f'{nome}', end=' ')
else:
    print('Não há mulheres cadastradas.')

if acim_med:
    print('\nLista de pessoas acima da media: ',end='')
    for nome in acim_med:
        print(f'{nome}', end=' ')
else:
    print('Não há pessoas acima da media de idade (30+).')