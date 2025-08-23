#Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
# No final mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno indevidualmente
alunos = []
medias = []
cont = 0

while True:
    nome = input('Nome: ').strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    medias.append([nota1, nota2])
    alunos.append([cont, nome, media])

    while True:
        opcao = ''
        opcao = input('Quer continuar? (S/N): ').strip().lower()[0]
        if opcao in 'n':
            break
        elif opcao == 's':
            break
        else:
            print('Opcao invalida!')
    if opcao == 'n':
        break

    cont += 1

print('-=' * 11)
print('No. Nome      Media')
print('-' * 22)
for aluno in range(cont + 1):
    print(f'{alunos[aluno][0]:<3}', end=' ')
    print(f'{alunos[aluno][1]:<10}', end=' ')
    print(f'{alunos[aluno][2]:<3}', end=' ')
    print()

print('-' * 22)
while True:
    no = int(input('Quer mostrar as notas de qual aluno? (999 interoompe): '))
    if no == 999:
        break
    elif no <= cont:
        print(f'As notas da(o) {alunos[no][1]} sao: {medias[no]}')
    else:
        print('Aluno nao cadastrado!')