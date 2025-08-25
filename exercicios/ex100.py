#Crie um programa que tenha uma lista chamada numeros e duas funcoes chamadas sorteio() e somar(). A primeira funcao vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda funcao vai mostrar a soma entre todos os valores pares sorteados pela funcao anterior
from random import randint

def sorteio(numeros):
    print('Sorteando 5 valores da lista: ', end='')
    for _ in range(5):
        num = randint(0, 9)
        numeros.append(num)
        print(num, end=' ')


def somar(numeros):
    soma_par = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma_par += numero
    print(f'\nSomando os valores pares de {numeros}, temos {soma_par}')


numeros = []
sorteio(numeros)
somar(numeros)
