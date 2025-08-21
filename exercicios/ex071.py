#Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual será o valor a ser sacado (numero inteiro) e o programa vai informar quantas celdulas de cada valor serao entregues
# Obs Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1
nota_50 = nota_20 = nota_10 = nota_1 = 0
montante = restante = 0
print('=#=' * 14)
print(' Seja bem vindo, ao seu caixa eletronico!')
print('=#=' * 14)

while True:
    valor_saque = 0
    while valor_saque <= 0:
        valor_saque = int(input('Digite o valor que deseja sacar: R$'))
        if valor_saque <= 0:
            print('Digite uma opcao valida!')

    if valor_saque >= 50:
        nota_50 = valor_saque // 50
        montante = valor_saque - (nota_50 * 50)
    else:
        montante = valor_saque

    if montante >= 20:
        nota_20 = montante // 20
        restante = montante - (nota_20 * 20)
    else:
        restante = montante

    if restante >= 10:
        nota_10 = restante // 10
        nota_1 = restante - (nota_10 * 10)
    else:
        nota_1 = restante

    break

print(f'\nVoce receberá R${valor_saque},00 em:')
print(f'{nota_50} notas de R$50,00')
print(f'{nota_20} notas de R$20,00')
print(f'{nota_10} notas de R$10,00')
print(f'{nota_1} notas de R$1,00')

