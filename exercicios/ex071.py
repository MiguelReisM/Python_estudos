#Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual será o valor a ser sacado (numero inteiro) e o programa vai informar quantas celdulas de cada valor serao entregues
# Obs Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1
print('=#=' * 14)
print(' Seja bem vindo, ao seu caixa eletronico!')
print('=#=' * 14)

valor_saque = 0
ced = 50

while valor_saque <= 0:
    valor_saque = int(input('Digite o valor que deseja sacar: R$'))
    if valor_saque <= 0:
        print('Digite uma opcao valida!')
    else:
        break
print(f'Voce receberá R${valor_saque},00 em: ')

restante = valor_saque

while restante > 0:
    qtd = restante // ced
    if qtd > 0:
        print(f'{qtd} nota(s) de R${ced},00')
    restante %= ced

    if ced == 50:
        ced = 20
    elif ced == 20:
        ced = 10
    elif ced == 10:
        ced = 1
    else:
        break

