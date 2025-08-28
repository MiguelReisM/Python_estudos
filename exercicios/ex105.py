#Crie um programa tenha uma funcao notas() que pode receber varias notas de alunos e vai retonar um dicionario com as seguintes informacoes:
# Quantidade de notas
# A maior nota
# A menor nota
# A media da turma
# A situacao (opcional)
#Adicione tambem docstrings da funcao
def notas(n1, n2, n3, n4, sit=False):
    """
    -> Função para analisar notas de alunos
    :param n1, n2, n3, n4: notas dos alunos
    :param sit: valor opcional, indica se deve ou não mostrar a situação
    :return: dicionário com várias informações
    """
    valores = [n1, n2, n3, n4]
    alunos = {'Total' : len(valores),
              'Maior nota' : max(valores),
              'Menor nota' : min(valores),
              'Media da turma' : sum(valores)/len(valores),}

    if sit:
        if sum(valores)/len(valores) >= 6:
            alunos['Situacao'] = 'Media Boa'
        else:
            alunos['Situacao'] = 'Media Ruim'

    return alunos


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
