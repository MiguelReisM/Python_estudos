#Crie um programa que leia um nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas minusculas
# Quatas letras ao todo (sem considerar espacos)
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print(f'O seu nome é: {nome}')
print(f'em maiusculo fica: {nome.upper()}')
print(f'em minusculo fica: {nome.lower()}')
print(f'ele tem {len(nome.replace(' ',''))} letras')
print(f'e o primeiro nome tem {len(nome.split()[0])} letras')

