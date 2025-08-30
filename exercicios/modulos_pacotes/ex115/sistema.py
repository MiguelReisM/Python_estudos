from pathlib import Path

_ARQUIVO = Path(__file__).with_name("dados.txt")

def menu():
    print('=-' * 20)
    print(f'{"MENU PRINCIPAL":^40}')
    print('=-' * 20)
    print('''\033[34m1 - Ver pessoas cadastradas\n2 - Cadastrar novas pessoas\n3 - Sair do sistema \033[m''')
    print('=-' * 20)


def cadastro():
    print('=-' * 20)
    print(f'{"NOVO CADASTRO":^40}')
    print('=-' * 20)

    nome = input('Digite seu nome: ').strip().title()

    while True:
            try:
                idade = int(input('Digite sua idade: '))
                if idade < 0:
                    print('\033[31mIdade inválida. Tente novamente.\033[m')
                else:
                    break
            except ValueError:
                print('\033[31mErro! Digite um número inteiro.\033[m')

    with _ARQUIVO.open("a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{idade}\n")

    print(f'Novo registro de {nome} de {idade} anos, adicionado com sucesso.')


def listar():
    print('=-' * 20)
    print(f'{"PESSOAS CADASTRADAS":^40}')
    print('=-' * 20)

    try:
        with _ARQUIVO.open("r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            if not linhas:
                print("\033[33mNenhuma pessoa cadastrada ainda.\033[m")
                return

            for linha in linhas:
                nome, idade = linha.strip().split(";")
                print(f"{nome:<30}{idade:>3} anos")

    except FileNotFoundError:
        print("\033[31mArquivo de dados não encontrado.\033[m")