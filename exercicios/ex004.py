#Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ela

digitacao = input('Digite algo: ')
print()
print(f'Voce digitou ({digitacao}) e isso é: ')
print(f'Ele é um(a): {type(digitacao)}')
print(f'Só tem espaços? {digitacao.isspace()}')
print(f'Ele é uma letra? {digitacao.isalpha()}')
print(f'Esta em letra maiuscula? {digitacao.isupper()}')
print(f'Esta em letra minuscula? {digitacao.islower()}')
print(f'Ele é um numero? {digitacao.isnumeric()}')
print(f'Ele é uformado por letras ou um numeros? {digitacao.isalnum()}')
