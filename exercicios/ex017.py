#Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. calcule e mostre o comprimento da hipotenusa
import math
cateto_op = float(input('Digite o cateto oposto: '))
cateto_ad = float(input('Digite o cateto adjacente: '))
hipotenusa = math.hypot(cateto_op, cateto_ad)

print(f'A hipotenusa do cateto adjacente {cateto_ad} e o cateto oposto {cateto_op} é {hipotenusa:.4f}')