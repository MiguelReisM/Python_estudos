#Crie um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
# Se ele ainda vai se alistar ao servico militar
# Se é a hora de se alistar
# Se ja passou o tempo do alistamento
# Seu programa tambem devera mostrar o tempo que falat ou que passou do prazo
from datetime import date

print('=-' * 20)
print('     Alistamento militar     ')
print('-' * 40)

ano = int(input('Informe o ano do seu nascimento: '))
alistamento = date.today().year - ano
if alistamento < 18:
    print(f'Ainda faltam {18 - alistamento} anos para se alistar')
elif alistamento > 18:
    print(f'Ja passou {alistamento - 18} anos do prazo do seu alistamento')
elif alistamento == 18:
    print('Chegou aos 18 anos, hora de se alistar!')