#Crie um programa que pergunte o salario e calcule o valor do seu aumento
# Para salario superiores a R$1.250,00 calcule um aumento de 10%
# Para inferiores ou iguais, o aumento é de 15%
salario = float(input('Digite o salario: '))

if salario > 1250:
    salario += (salario * 0.10)
    print(f'O novo salario é de R${salario:.2f} já com o aumento de 10%')
else:
    salario += (salario * 0.15)
    print(f'O novo salario é de R${salario:.2f} já com o aumento de 15%')