#Crie um programa que tenha a funcao leiaint() que vai funcionar semelhante a funcao input() do Python, só que fazendo validacao para aceitar apenas valores numerico
# ex: n = leiaInt('Digite um n)
def leiaInt(msg):
    while True:
        n = input(msg)
        if n.strip().lstrip('-').isnumeric():
            return int(n)
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')