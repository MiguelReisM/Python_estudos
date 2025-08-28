from modulos_pacotes.moeda import moeda

preco = float(input('Digite o preco: R$ '))
print(f'A metade de R${preco:.2f} é R${moeda.metade(preco):.2f}')
print(f'O dobro de R${preco:.2f} é R${moeda.dobro(preco):.2f}')
print(f'O valor de R${preco:.2f} com 10% de aumento é R${moeda.aumentar(preco):.2f}')
print(f'O valor de R${preco:.2f} com 13% de desconto é R${moeda.diminuir(preco):.2f}')