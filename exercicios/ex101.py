#Crie um programa que tenha uma funcao chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retronando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleicoes
def voto(ano):
    from datetime import date

    idade = date.today().year - ano

    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


ano_nasc = int(input('Digite o seu ano de nascimento: '))
print(voto(ano_nasc))
