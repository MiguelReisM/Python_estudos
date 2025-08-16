#Crie um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 por cada Km acima do limite
velocida = int(input('Digite a velocidade do carro ao passar no radar: '))
multa = velocida - 80

if velocida > 80:
    multa = float(multa * 7)
    print(f'Voce ultrapassou o limite de velocidade e será multado em R${multa:.2f}')
