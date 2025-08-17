#Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida:
# Media abaixo de 5.0 - Reprovado
# Media entre 5.0 e 6.9 - Recuperacao
# Media 7.0 ou superior - Aprovado
num1 = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segunda nota: '))
media = (num1 + num2) / 2

if media < 5.0:
    print(f'A media final foi {media}, voce esta reprovado!')
elif media >= 5 and media < 7:
    print(f'Sua media foi {media}, voce esta de recuperacao!')
else:
    print(f'Voce foi aprovado! Sua media foi {media}')