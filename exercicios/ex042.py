#Crie um programa que leia o comprimento de 3 retas e diga ao ususario se elas podem ou nao formar um triangulo, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
# - Equilatero: todos os lados iguais
# - Isosceles: dois lados iguais
# - Escaleno: todos os lados diferentes
a = float(input('Informe o valor do lado A do triangulo: '))
b = float(input('Informe o valor do lado B do triangulo: '))
c = float(input('Informe o valor do lado C do triangulo: '))
formou = False

if a + b > c and a + c > b and b + c > a:
    print('Foi possivel gerar um triangulo com essas retas!')
    formou = True
    if formou == True and a == b == c:
        print('O seu triangulo é Equilatero')
    elif formou == True and a != b != c:
        print('O seu triangulo é Escaleno')
    else:
        print('O seu triangulo é Isosceles')
else:
    print('Nao foi possivel gerar um triangulo com essas retas!')
