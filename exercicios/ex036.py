#Crie um programa para aprovar o meprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantas anos ele vai pagar.
# Calcule o valor da prestacao mensal sabendo que nao pode execer 30% do salario ou netao o emprestimo será negado.
print('=-' * 20)
print('     Aprovador de emprestimo     ')
print('-' * 40)
valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Agora me informe seu salario: R$'))
anos_pagamento = int(input('Em quantos anos voce deseja pagar esse imovel? '))
print('=-' * 20)

prestcao = valor_casa / (anos_pagamento * 12)

if prestcao < (salario * 0.30):
    print(f'O emprestimo foi aprovado! \nO imovel de R${valor_casa:.2f}, será pago em {(anos_pagamento * 12)} meses, \ne o valor das prestcoes será de R${prestcao:.2f}.')
else:
    print(f'Infelizmente a prestacao de R${prestcao:.2f} ultrapaca 30% do seu salario de R${salario}, e o imprestimo foi negado!')