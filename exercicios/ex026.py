#Crie um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posicao ela aparece a primeira vez
# Em que posicao ela aparece a ultima vez.
frase = str(input('Digite uma frase: ')).strip().lower()
aparecer = frase.count('A')
primeira_vez = frase.find('A')
ultima_vez = frase.rfind('A')

print(f'A letra "A" aparece {aparecer} vezes')
print(f'A letra "A" aparece pela primeira vez na posicao {primeira_vez}')
print(f'A letra "A" aparece pela ultima vez na posicao {ultima_vez}')