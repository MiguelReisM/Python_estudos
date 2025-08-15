#Crie um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
# ex: Digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1
numero = int(input('Digite um numero de 0 até 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'No numero {numero} temos:')
print(f'unidade: {unidade}')
print(f'dezena: {dezena}')
print(f'centena: {centena}')
print(f'milhar: {milhar}')