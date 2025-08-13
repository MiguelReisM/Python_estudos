#Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m^2
largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = altura * largura

print(f'Como a altura da sua parede é de {altura:.2f}M e {largura:.2f}M de largura, será necessario {area/2} litros de tinta')