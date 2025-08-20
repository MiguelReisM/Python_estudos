#Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condicao de parada. No final mostre quantos numeros foram digitados e qual foi a soma entre eles, desconsiderando o 999
num = cont = soma = 0

while num != 999:
    num = int(input('Digite um numero inteiro [digite 999 caso queira parar]: '))
    cont += 1
    soma += num
print(f'Voce digitou {cont-1} numero(os) e a somatoria deles é {soma-999}')