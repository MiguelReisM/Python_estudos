#Crie um programa que leia quanto dinheiro uma pessoa tem na corteira e mostre quantos Dolares ela pode comprar.
#Considere US$ 1,00 = R$ 5.40
carteira = float(input('Digite quanto tem na sua carteira: '))
dolares = (carteira / 5.40)

print(f'Voce pode comprar US${dolares:.2f} dolares com R${carteira:.2f} reais')