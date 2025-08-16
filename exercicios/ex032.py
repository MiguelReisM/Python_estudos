#Crie um programa que leia um ano qualquer e mostre se ele é BISSEXTO
ano = int(input('Digite o ano: '))
centenario = ano % 100
bissexto = ano % 4

if bissexto == 0:
    if (ano % 4 == 0 & ano % 100 != 0) or (ano % 400 == 0):
        print(f'O ano {ano} é bissexto')
    else:
        print(f'O ano {ano} ñ é bissexto')

else:
    print(f'O ano {ano} não é bissexto')
