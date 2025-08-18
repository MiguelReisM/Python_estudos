#Crie um programa que calcule a soma entre todos os numeros impares que sao multiplos de 3 e que se encontram de 1 ate 500
resultado = 0

for n in range(3, 500+1, 6):
    resultado += n
print(f'O resultado da soma é: {resultado}')