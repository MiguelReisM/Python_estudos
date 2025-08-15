#Crie um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# ex: Ana Maria de Souza
# Primeiro = Ana
# Ultimo = Souza
nome = str(input('Digite seu nome completo: ')).lower().title().strip()
contagem = nome.split()
primeiro = contagem[0]
ultimo = (contagem[len(contagem)-1])

print('Analisando nome...')
print(f'Seu primeiro nome é: {primeiro}')
print(f'Seu ultimo nome é: {ultimo}')