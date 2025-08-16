#Crie um programa que pergunte a distancia de uma viagem em Km. Calcule o preco da passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas
quilometragem = float(input('Digite quantos Km tem o seu percurso de viagem: '))

if quilometragem > 0:
    if quilometragem <= 200:
        preco = quilometragem * 0.50
        print(f'O preco da viagem ficou R${preco:.2f}')
    else:
        preco = quilometragem * 0.45
        print(f'O preco da viagem ficou R${preco:.2f}')
else:
    print('Digite uma Km valida!')