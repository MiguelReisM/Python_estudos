#Adpte o codigo do desafio 107 criando uma funcao adicional chamada moeda() que consiga mostrar os valores como valor monetario formatado
from modulos_pacotes.moeda import moeda_formatada

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda_formatada.moeda(preco)} é {moeda_formatada.moeda(moeda_formatada.metade(preco))}')
print(f'O dobro de {moeda_formatada.moeda(preco)} é {moeda_formatada.moeda(moeda_formatada.dobro(preco))}')
print(f'O valor de {moeda_formatada.moeda(preco)} com 10% de aumento é {moeda_formatada.moeda(moeda_formatada.aumentar(preco))}')
print(f'O valor de {moeda_formatada.moeda(preco)} com 13% de desconto é {moeda_formatada.moeda(moeda_formatada.diminuir(preco))}')
