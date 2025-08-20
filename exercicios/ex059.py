#Crie um programa que leia 2 valores e mostre um menu na tela:
# 1 soma
# 2 multiplicar
# 3 maior
# 4 novos numeros
# 5 sair do programa
# Seu programa devera realizar a oprecao solicitada em cada caso.
opcao = 0
num1 = num2 = 0
maior = menor = 0

while opcao != 5:
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    opcao = 0
    while opcao != 4 and opcao != 5:
        opcao = int(input('\nDigite a opcao desejada:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos numeros\n[5] Sair do programa\n Opcao desejada: '))
        if opcao == 1:
            print(f'\nA soma de {num1} + {num2} = {num1 + num2}')
        if opcao == 2:
            print(f'\nA multiplicacao de {num1} x {num2} = {num1 * num2}')
        if opcao == 3:
            if num1 > num2:
                maior = num1
                menor = num2
                print(f'\nO maior valor é {maior} e o menor {menor}')
            elif num1 == num2:
                print(f'\nOs numeros {num1} e {num2} sao iguais')
            else:
                maior = num2
                menor = num1
                print(f'\nO maior valor é {maior} e o menor {menor}')
print('Encerrado!')