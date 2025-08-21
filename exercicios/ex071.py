#Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual será o valor a ser sacado (numero inteiro) e o programa vai informar quantas celdulas de cada valor serao entregues
# Obs Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1
valor_saque = -1
nota_50 = nota_20 = nota_10 = nota_1 = 0

print('=#=' * 14)
print(' Seja bem vindo, ao seu caixa eletronico!')
print('=#=' * 14)

while True:
    while valor_saque < 0:
        valor_saque = int(input('Digite o valor que deseja sacar: R$'))
        if valor_saque < 0:
            print('Digite uma opcao valida!')

    if valor_saque > 50:
        nota_50 = valor_saque // 50
print(f'Voce receberá {valor_saque} em:')
print(f'X notas de {nota_1}')

