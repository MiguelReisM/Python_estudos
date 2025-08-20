#Crie um programa que leia 2 valores e mostre um menu na tela:
# 1 soma
# 2 multiplicar
# 3 maior
# 4 novos numeros
# 5 sair do programa
# Seu programa devera realizar a oprecao solicitada em cada caso.
while True:
    num1 = int(input('\nDigite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    while True:
        print("\n===== MENU =====")
        print("[1] Somar")
        print("[2] Multiplicar")
        print("[3] Maior")
        print("[4] Novos números")
        print("[5] Sair do programa")

        opcao = int(input("Opção desejada: "))

        if opcao == 1:
            print(f'\nA soma de {num1} + {num2} = {num1 + num2}')
        elif opcao == 2:
            print(f'\nA multiplicação de {num1} x {num2} = {num1 * num2}')
        elif opcao == 3:
            if num1 > num2:
                print(f'\nO maior valor é {num1} e o menor é {num2}')
            elif num2 > num1:
                print(f'\nO maior valor é {num2} e o menor é {num1}')
            else:
                print(f'\nOs números {num1} e {num2} são iguais')
        elif opcao == 4:
            # volta para digitar novos números
            break
        elif opcao == 5:
            print('\nPrograma encerrado!')
            exit()
        else:
            print('\nOpção inválida, tente novamente.')
