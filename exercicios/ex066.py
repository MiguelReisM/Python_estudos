#Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que é a condicao de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles, descondire o flag
somatoria = cont = 0

while True:
    num = int(input('Digite um numero inteiro, caso deseje parar digite 999: '))
    if num == 999:
        break
    somatoria += num
    cont += 1
print(f'Foram digitados {cont} numeros e a somatoria deles deu: {somatoria}')