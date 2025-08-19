#Crie um programa que leia o ano de nascimento de 7 pessoas. No final mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja atingiram
from datetime import date

maior = 0
menor = 0

for p in range(1, 8):
    ano = int(input((f'Por gentileza a {p}° pessoa informe o seu ano de nascimento: ')))
    if  date.today().year - ano >= 18:
        maior += 1
    else:
        menor += 1
print(f'{menor} pessoa(as) nao atingiram a maioridade, e {maior} pessoa(as) já atingiram a maioridade')