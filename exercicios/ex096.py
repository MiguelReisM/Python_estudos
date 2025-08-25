#Crie um programa que tenha uma funcao chamada area(). que receba as dimensoes de um terreno retangular (largura e comprimento) e mostre a area do retangulo
def area(larg, comp):
    area = larg * comp
    print(f'A area desse terreno é {area:.1f} metros quadrados')


larg = float(input('Digite a largura do terreno (M): '))
comp = float(input('Digite o comprimento do terreno (M): '))
area(larg, comp)