#Crie um algoritmo que leia o salario com 15% de aumento
salario = float(input('Digite o salario: '))
aumento = salario + (salario * 0.15)

print(f'O salario com 15% de aumento fica R${aumento:.2f}')