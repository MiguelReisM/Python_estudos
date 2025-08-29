#Modifique as funcoes que foram criadas no desafio 107 para que elas aceitem um parametro a mais, informando se o valor vai ser formatado pela funcao moeda(), desevolvida no desafio 108
from modulos_pacotes.moeda import moeda_formatada

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda_formatada.moeda(preco)} é {moeda_formatada.moeda(moeda_formatada.metade(preco))}')
print(f'O dobro de {moeda_formatada.moeda(preco)} é {moeda_formatada.moeda(moeda_formatada.dobro(preco))}')
print(f'O valor de {moeda_formatada.moeda(preco)} com 10% de aumento é {moeda_formatada.moeda(moeda_formatada.aumentar(preco))}')
print(f'O valor de {moeda_formatada.moeda(preco)} com 13% de desconto é {moeda_formatada.moeda(moeda_formatada.diminuir(preco))}')