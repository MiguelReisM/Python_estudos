#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = str(input('Digite seu nome completo: ')).lower().title().strip().split()
silva = ('Silva') in nome
print('No seu nome encontramos "Silva" ?')
print(silva)

