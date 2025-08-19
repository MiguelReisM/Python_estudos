#Crie um programa que leia um numero inteiro qualquer e mostre na tela sua tabuada usando um laco for
num = int(input('Digite um numero para ver sua tabuada: '))

for n in range(1, 11):
    print(f'({n}) X ({num}) = {n * num}')
