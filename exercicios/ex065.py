#Crie um programa que leia varios numeros inteiros pelo teclado. No final da execucao, mostre a media entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao ususario se ele quer ou nao continuar a digitar valores
condicao = 'S'
num = somatoria = cont = 0
maior = menor = 0
while condicao != 'N':
    num = int(input('Digite um numero: '))
    if cont == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < maior:
            menor = num
    somatoria += num
    cont += 1
    condicao = input('Voce deseja continuar? (S/N): ').strip().upper()
print(f'A media deu {somatoria/cont}')
if maior == menor:
    print(f'Os numeros {num} e {num} sao iguais, ou seja nao existe maior e menor')
else:
    print(f'O maior numero foi {maior} e o menor foi {menor}')