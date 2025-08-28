#Adpte o codigo do desafio 107 criando uma funcao adicional chamada moeda() que consiga mostrar os valores como valor monetario formatado
from modulos_pacotes.moeda import moeda

preco = float(input('Digite o preco: R$ '))
print(f'A metade de R${preco} é R${moeda.metade(preco)}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'O valor de R${preco} com 10% de aumento é R${moeda.aumentar(preco)}')
print(f'O valor de R${preco} com 13% de desconto é R${moeda.diminuir(preco)}')