#Crie um programa que tenha uma tupla unica com nomes de seus produtos e seus respectivos precos, na sequencia
# No final mostre uma listagem de precos organizando os dados em forma tabular
print('=-=' * 15)
print(f'{"Listagem de preços":^45}')
print('=-=' * 15)

lista = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)

c2 = 0
for c1, i in enumerate(lista):
    if c1 % 2 == 0:
        print(f'{lista[c1]:.<34} R${lista[c1+1]:>7.2f}')
print('=-=' * 15)