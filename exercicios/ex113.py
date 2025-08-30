#Crie um programa que tenha a funcao leiaint() que vai funcionar semelhante a funcao input() do Python, só que fazendo validacao para aceitar apenas valores numerico
# ex: n = leiaInt('Digite um n)
# Rescreva a funcao leiaInt() que fizemos no desafio 104, incluindo a possibilidade da digitacao de um numero de tipo invalido.
# Aproveite e crie tamebm uma funcao leiaFloat() com a mesma funcionalidade
def leiaInt(msg):
    while True:
        ni = input(msg).strip()
        try:
            return int(ni)
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mErro! O usuario preferiu nao digitar o valor.\033[m')


def leiaFloat(msg):
    while True:
        nf = input(msg).strip().replace(',','.')
        try:
            return float(nf)
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número float válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mErro! O usuario preferiu nao digitar o valor.\033[m')



ni = leiaInt('Digite um numero: ')
nf = leiaFloat('Digite um flot: ')
print(f'Os valores digitados foram: {ni} e {nf:.2f}')