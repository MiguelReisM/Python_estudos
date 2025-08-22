#Crie um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# quantas vezes apareceu o valor 9
# em que posicao foi digitado o primeiro valor 3
# quais foram os numeros pares
tupla_num = (int(input('Digite seu numero o primeiro numero: ')),
             int(input('Digite seu numero o segundo numero: ')),
             int(input('Digite seu numero o terceiro numero: ')),
             int(input('Digite seu numero o quarto numero: ')))
print(f'\nVoce digitou: {tupla_num}')

if tupla_num.count(9) != 0:
    print(f'- O numero 9 aparece {tupla_num.count(9)} vez(es)')
else:
    print('- O numero 9 nao aparece')

if tupla_num.count(3) != 0 and tupla_num.count(3) >= 2:
    print(f'- O numero 3 aparece primeiro na {tupla_num.index(3) + 1} posicao')
elif tupla_num.count(3) != 0 and tupla_num.count(3) == 1:
    print(f'- O numero 3 apareceu na {tupla_num.index(3) + 1} posicao')
else:
    print('- O numero 3 nao aprece')

print('- Esse(es) foram os numeros pares: ', end='')
for n in tupla_num:
    if n % 2 == 0:
        print(n, end=' ')


