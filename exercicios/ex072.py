#Crie um programa que leia uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
# Seu programa deverá ler um numero pelo teclado (entre 0 e 20 e mostra-lo por extenso)
numeros_extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    numeros = int(input('Digite um numero de 0 a 20: '))
    if numeros <= 20 and numeros >= 0:
        break
    else:
        print('Opcao invalida!')
print(f'{numeros_extenso[numeros]}')