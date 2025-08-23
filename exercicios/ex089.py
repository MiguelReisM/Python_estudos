#Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
# No final mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno indevidualmente
alunos = []

while True:
    nome = input('Nome: ').strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])

    opcao = input('Quer continuar? (S/N): ').strip().lower()
    if opcao == 'n':
        break

print('-=' * 11)
print(f'{"No.":<4}{"Nome":<10}{"Media":>6}')
print('-' * 22)

for i, aluno in enumerate(alunos):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>6.1f}')

print('-' * 22)

while True:
    no = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if no == 999:
        break
    elif 0 <= no < len(alunos):
        print(f'As notas de {alunos[no][0]} sao: {alunos[no][1]}')
    else:
        print('Aluno nao cadastrado!')
