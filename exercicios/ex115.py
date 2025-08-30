#Crie um pequeno sistema modularizado que permita cadastrar pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opcoes: cadastrar uma nova pessoa e listar todas as pessoas cadastradas
from modulos_pacotes.ex115 import sistema

while True:
    sistema.menu()
    while True:
        try:
            opcao = int(input('Sua opcao: '))
            if opcao not in (1, 2, 3):
                print('\033[31mErro! Digite uma opcao valida.\033[m')
            else:
                break
        except ValueError:
            print('\033[31mErro! Digite um numero.\033[m')

    if opcao == 3:
        print('Saindo do sistema... Até logo!')
        break
    elif opcao == 2:
        sistema.cadastro()
    else:
        sistema.listar()