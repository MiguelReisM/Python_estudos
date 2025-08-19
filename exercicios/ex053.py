#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espacos
print('Analisador de palindromos!')
frase = input('Digite sua frase: ').lower()
frase = frase.replace(' ','')
frase = (frase)
c = len(frase)
formou = True

for n in range(0, c):
    if frase[n] != frase[c-1]:
        formou = False
        break
    c -= 1

if formou == True:
    print('Formou um palindromo!')
else:
    print('Nao formou um palindromo')