#Crie um programa que tenha uma tupla com varias palavras (nao usar acentos).
# Depois disso, voce devera mostrar para cada palavra quais sao suas vogais.
palavras = (
    'aprender',
    'programar',
    'linguagem',
    'python',
    'curso',
    'gratis',
    'estudar',
    'praticar',
    'trabalhar',
    'mercado',
    'programador',
    'futuro'
)

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')