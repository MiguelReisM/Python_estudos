#Crie um programa que leia dois numeros inteiros e compare-os, mostarndo na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Nao existe valor maior, os dois sao iguais
print('=-' * 20)
print('     Verificando valores     ')
print('-' * 40)
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
print('=-' * 20)
print('     analisando...       ')
print('=-' * 20)

if num1 > num2:
    print(f'O primeiro valor ({num1}) é maior que o segundo valor ({num2})')
elif num2 > num1:
    print(f'O segundo valor ({num2}) é maior que o primeiro valor ({num1})')
else:
    print(f'Os valores {num1} e {num2} sao iguais')
