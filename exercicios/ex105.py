#Crie um programa tenha uma funcao notas() que pode receber varias notas de alunos e vai retonar um dicionario com as seguintes informacoes:
# Quantidade de notas
# A maior nota
# A menor nota
# A media da turma
# A situacao (opcional)
#Adicione tambem docstrings da funcao
def notas(*n, sit=False):
    """
    -> Função para analisar notas de alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indica se deve ou não mostrar a situação.
    :return: dicionário com várias informações sobre as notas.
    """
    alunos = {'Total' : len(n),
              'Maior nota' : max(n),
              'Menor nota' : min(n),
              'Media da turma' : sum(n)/len(n),}

    if sit:
        if sum(n)/len(n) >= 6:
            alunos['Situacao'] = 'Media Boa'
        else:
            alunos['Situacao'] = 'Media Ruim'

    return alunos


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
