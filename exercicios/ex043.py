#Crie uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima dos 40: Obsidade morbida
tipos_imc = ['Abaixo do peso', 'Peso ideal', 'Sobrepeso', 'Obesidade', 'Obsidade morbida']
altura = float(input('Digite sua altura em cm: '))
peso = float(input('Digite seu peso em Kg: '))
imc = peso / (altura / 100 ) ** 2

if imc < 18.5:
    print(f'O seu IMC de {imc:.2f} se configura em {tipos_imc[0]}')
elif imc >= 18.5 and imc < 25:
    print(f'O seu IMC de {imc:.2f} se configura em {tipos_imc[1]}')
elif imc >= 25 and imc < 30:
    print(f'O seu IMC de {imc:.2f} se configura em {tipos_imc[2]}')
elif imc >= 30 and imc < 40:
    print(f'O seu IMC de {imc:.2f} se configura em {tipos_imc[3]}')
else:
    print(f'O seu IMC de {imc:.2f} se configura em {tipos_imc[4]}')