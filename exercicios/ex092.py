#Crie um programa que leie o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario se por acaso a CTPS,
# for diferente de ZERO. o dicionario recebra tambem o ano de contratacao e o salrio. Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar (=35 anos de contratacao)
from datetime import date

pessoas = {}

pessoas['nome'] = input('Digite nome: ').strip().title()
ano_nasc = int(input('Digite o ano que nasceu: '))
pessoas['idade'] = (date.today().year - ano_nasc)
pessoas['ctps'] = int(input('Carteira de trabalho (0 nao tem): '))

if pessoas['ctps'] != 0:
    pessoas['ano_contrat'] = int(input('Ano contratacao: '))
    pessoas['salario'] = float(input('Digite o salario: R$'))
    pessoas['aposentadoria'] = ((pessoas['ano_contrat'] - ano_nasc) + 35)

print(f'\nNome tem o valor: {pessoas["nome"]}')
print(f'Idade tem o valor: {pessoas["idade"]} anos')
print(f'CTPS tem o valor: {pessoas["ctps"]}')

if pessoas['ctps'] != 0:
    print(f'Ano contratacao tem o valor: {pessoas["ano_contrat"]}')
    print(f'Salario tem o valor: R${pessoas["salario"]:.2f}')
    print(f'Aposentadoria tem o valor: {pessoas["aposentadoria"]} anos')