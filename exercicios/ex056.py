#Crie um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A media de idade do grupo
# Qual o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos
from datetime import date

nome_h = 'nenhum'
idade_h = 0
idade_m = 0
total = 0

for p in range(1, 5):
    print(f'Por gentileza a {p}° pessoa informe os dados a seguir:')
    nome = input('Digite seu nome: ').strip().title()
    idade = int(input('Digite sua idade: '))
    sexo = input('Sexo [M/F]: ').lower().replace('','')
    total += idade
    if sexo == 'm' and idade_h < idade:
        idade_h = idade
        nome_h = nome
    elif sexo == 'f' and idade < 20:
        idade_m += 1

print(f'A media de idade desse grupo de pessoas ficou: {total / 4}')
print(f'O nome do homem mais velho é {nome_h} e a idade dele é {idade_h}')
print(f'Tem {idade_m} mulheres menores de 20 anos')

