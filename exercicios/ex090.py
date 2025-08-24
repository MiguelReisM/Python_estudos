#Crie um programa que leia o nome e media de um aluno, guardando tambem a situacao em um dicionario. (media >= 6 aprovado)
# No final mostre o conteudo da estrutura na tela
aluno = {}

aluno['nome'] = input('Digite o nome: ')
aluno['media'] = float(input('Digite a media: '))

if aluno['media'] >= 6:
    aluno["situacao"] = 'Aprovado'
else:
    aluno["situacao"] = 'Reprovado'

print('-' * 30)
for k, v in aluno.items():
    print(f'{k.title()}: {v}')
