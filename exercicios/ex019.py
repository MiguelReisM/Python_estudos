#Crie um codigo onde um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido
import random

aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

aluno_aleatorio = random.choice(alunos)

print(f'O aluno escolhido foi {aluno_aleatorio}')