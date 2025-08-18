#Crie um programa que leia um numero inteiro qualquer e mostre na tela sua tabuada usando um laco for
num = int(input('Digite um numero para ver sua tabuada: '))
resultado = 0
for n in range(1, 11):
    resultado = n * num
    print(f'({n}) X ({num}) = {resultado}')
