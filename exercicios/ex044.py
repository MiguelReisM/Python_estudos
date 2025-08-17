#Crie um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de pagamento:
# A vista dinheiro/cheque: 10% de desconto
# A vista no cartao: 5% de desconto
# Ate 2x no cartao: preco normal
# 3x ou mais no cartao 20% de juros
valor_produto = float(input('Digite o valor do produto: '))
tipo_pagamento = int(input('\nSelecione o metodo de pagamento:\n1 - Dinheiro ou cheque:\n2 - A vista no cartao:\n3 - Em 2x no cartao sem juros:\n4 - 3x ou mais no cartao (juros de 20%):\nOpcao escolhida: '))

if tipo_pagamento >= 1 and tipo_pagamento <= 4:
    if tipo_pagamento == 1:
        print(f'\nVoce escolheu a opcao {tipo_pagamento} - A vista dinheiro/cheque e terá 10% de desconto\nO valor do seu produto ficará: R${(valor_produto - valor_produto * 0.1):.2f}')
    elif tipo_pagamento == 2:
        print(f'\nVoce escolheu a opcao {tipo_pagamento} - A vista no cartao e terá 5% de desconto\nO valor do seu produto ficará: R${(valor_produto - valor_produto * 0.05):.2f}')
    elif tipo_pagamento == 3:
        print(f'\nVoce escolheu a opcao {tipo_pagamento} - Ate 2x no cartao, opcao nao aplicavel a desconto\nO valor do seu produto ficará: R${valor_produto:.2f}')
    elif tipo_pagamento == 4:
        print(f'\nVoce escolheu a opcao {tipo_pagamento} - 3x ou mais no cartao e terá 20% de juros\nO valor do seu produto ficará: R${(valor_produto + valor_produto * 0.20):.2f}')
else:
    print('Escolha uma opcao valida!')