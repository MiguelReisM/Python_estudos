#Modifique as funcoes que foram criadas no desafio 107 para que elas aceitem um parametro a mais, informando se o valor vai ser formatado pela funcao moeda(), desevolvida no desafio 108
from modulos_pacotes.moeda import moeda

preco = float(input('Digite o preco: R$ '))
print(f'A metade de R${preco} é R${moeda.metade(preco)}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'O valor de R${preco} com 10% de aumento é R${moeda.aumentar(preco)}')
print(f'O valor de R${preco} com 13% de desconto é R${moeda.diminuir(preco)}')