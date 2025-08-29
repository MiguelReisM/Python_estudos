#Adpte o codigo do desafio 107 criando uma funcao adicional chamada moeda() que consiga mostrar os valores como valor monetario formatado
from modulos_pacotes.moeda import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'O valor de {moeda.moeda(preco)} com 10% de aumento é {moeda.moeda(moeda.aumentar(preco))}')
print(f'O valor de {moeda.moeda(preco)} com 13% de desconto é {moeda.moeda(moeda.diminuir(preco))}')
