#Crie um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto.
preco = float(input('Digite o valor do produto (R$): '))
desconto = preco - (preco * 0.05)

print(f'O novo valor desse produto com 5% de desconto é: R${desconto:.2f}')