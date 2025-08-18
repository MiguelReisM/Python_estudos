#Crie um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar desconsidere-o
resultado = 0
num = 0

for n in range(1, 7):
    num = int(input(f'Digite o {n}° numero: '))
    if num % 2 == 0:
        resultado += num
print(f'A somatoria de pares deu: {resultado}')