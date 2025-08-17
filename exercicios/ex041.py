#Crie um programa, a confederacao de natacao nacional de natacao precisa que o programa leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - ate 9 anos: Mirim
# - ate 14 anos: Infantil
# - ate 19 anos: Junior
# - acima: Master
from datetime import date
categoria = ['Mirim', 'Infantil', 'Junior', 'Master']
nascimento = int(input('Digite o seu ano de nascimento: '))
ano = date.today().year

if ano - nascimento < 9:
    print(f'O nadador cadastrado tem {ano - nascimento} anos, ele está na categoria {categoria[0]}')
elif ano - nascimento < 14:
    print(f'O nadador cadastrado tem {ano - nascimento} anos, ele está na categoria {categoria[1]}')
elif ano - nascimento < 19:
    print(f'O nadador cadastrado tem {ano - nascimento} anos, ele está na categoria {categoria[2]}')
else:
    print(f'O nadador cadastrado tem {ano - nascimento} anos, ele está na categoria {categoria[3]}')
