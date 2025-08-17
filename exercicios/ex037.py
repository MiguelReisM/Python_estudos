#Crie um programa que leia um numero inteiro qualquer e preca para o usuario escolher qual sera a base de conversao:
# 1 - para binario
# 2 - para octal
# 3 - para hexadecimal
print('=-' * 20)
print('     Bases de conversao     ')
print('-' * 40)
numero = int(input('Digite um numero inteiro: '))
print(f'Certo agora que voce digitou {numero}, escolha qual \nopcao voce deseja fazer sua conversao: ')
opcao = int(input(' 1 - para binario\n 2 - para octal\n 3 - para hexadecimal\nOpcao:'))
print('=-' * 20)

if opcao == 1:
    print(f'A conversao para binario fica: {bin(numero)[2:]}')
elif opcao == 2:
    print(f'A conversao para octal fica: {oct(numero)[2:]}')
elif opcao == 3:
    print(f'A conversao para hexadecimal fica: {hex(numero)[2:]}')
else:
    print('Digite uma opcao valida!')