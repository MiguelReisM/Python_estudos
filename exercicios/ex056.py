#Crie um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A media de idade do grupo
# Qual o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos
for p in range(1, 5):
    print(f'Por gentileza a {p}° pessoa informe os dados a seguir:')
    nome = input('Digite seu nome: ').strip()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite m se voce for mulher e h se for homem: ').lower().replace('','')


