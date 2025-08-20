#Crie um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitadopelo usuario. O programa sera interrompido quando for solicitado um numero negativo.
while True:
    print('=-'*20)
    num = int(input('Digite um numero para ver sua tabuada, \ncaso deseje sair digite um numero negativo: '))
    cont = 1
    print('=-'*20)
    if num < 0:
        print('Programa encerrado!')
        break
    while cont <= 10:
        print(f'{num} X {cont} = {num * cont}')
        cont += 1
