#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espacos
print('Analisador de palindromos!')
frase = input('Digite sua frase: ').lower().replace(' ','')
c = len(frase)
formou = True

for n in range(c // 2):
    if frase[n] != frase[c - n - 1]:
        formou = False
        break

if formou == True:
    print('Formou um palindromo!')
else:
    print('Nao formou um palindromo')