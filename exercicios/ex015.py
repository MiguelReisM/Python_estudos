#Crie um codigo que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado
dias = int(input('Digite quantos dias voce ficou com o carro alugado: '))
km = float(input('Digite a Km percorrida neste periodo: '))
preco = (dias * 60) + (km * 0.15)

print(f'O valor a ser pago é de R${preco:.2f}')