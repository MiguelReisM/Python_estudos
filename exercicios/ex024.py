#Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com nome "Santo"
cidade = str(input('Digite a cidade em que voce nasceu: ')).strip().split()
primeiro_nome = cidade[0].lower().capitalize()
print(f'A cidade que voce nasceu comeca com Santo? ')
print(f'(Sim = 0), (Não = -1):  {primeiro_nome.find('Santo')}')