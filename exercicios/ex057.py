#Crie um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F Caso esteja errado, peca a digitacao novamente até ter um valor correto.
sexo = ''
while sexo != 'm' and sexo != 'f':
    sexo = input('Por gentileza informeu seu sexo (M/F): ').strip().lower()
print('Fim!')