#Crie um programa que leia o nome e o preco de varios produtos. O programa devera perguntar se o ususario vai continuar. No final mostre
# qual é o total gasto na compra
# quantos produtos custam mais de R$1000
# qual o nome do produto mais barato
num_produtos = total_gasto = produtos_caro = 0
menor_valor_produto = 0.0
produto_barato = ''

print('=-' * 20)

while True:
    num_produtos += 1
    nome_produto = input('Digite o nome do produto: ').strip().title()

    valor_produto = 0.0               # <<< reseta aqui
    while valor_produto <= 0:
        valor_produto = float(input('Digite o valor do produto: R$ '))
        if valor_produto <= 0:
            print('Valor inválido! Digite um número positivo.')

    total_gasto += valor_produto

    if valor_produto > 1000:
        produtos_caro += 1

    if num_produtos == 1 or valor_produto < menor_valor_produto:
        produto_barato = nome_produto
        menor_valor_produto = valor_produto

    opcao = ''
    while opcao not in ('s', 'n'):
        opcao = input('\nVocê deseja continuar? (S/N): ').strip().lower()[:1]

    if opcao == 'n':
        break

print('=-' * 20)
print(f'Dentre {num_produtos} produto(s), o total gasto foi de R$ {total_gasto:.2f}.')
print(f'{produtos_caro} produto(s) custam mais de R$ 1000,00.')
print(f'O produto mais barato foi {produto_barato}, custando R$ {menor_valor_produto:.2f}.')
