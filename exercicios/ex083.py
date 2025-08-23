#Crie um programa onde o usuario digite uma expressao qualquer que use parenteses.
# Seu aplicativo devera analisar se a expressao passada está com os parenteses abertos e fechados na ordem correta
expressao = input('Digite sua expressao matematica: ').replace(' ','')

parenteses_aberto = expressao.count('(')
parenteses_fechado = expressao.count(')')

if parenteses_aberto == parenteses_fechado:
    print('Essa expressao é valida!')
else:
    print('Essa expressao é invalida!')
