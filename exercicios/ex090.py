#Crie um programa que leia o nome e media de um aluno, guardando tambem a situacao em um dicionario. No final mostre o conteudo da estrutura na tela
aluno = {'nome' : '',
         'media' : 0.0}

aluno['nome'] = input('Digite o nome: ')
aluno['media'] = float(input('Digite a media: '))
print(f'O nome é {aluno["nome"]}')
print(f'A média é {aluno["media"]}')
if aluno['media'] >= 6:
    print('Situacao aprovado!')
else:
    print('Situacao reprovado!')
