#Crie um programa que leia o primeiro termo e a razao de uma PA (progressao aritmetica). No final, mostrando os 10 primeiros termos desse programa
pt = int(input('Digite o primeiro termo dessa PA: '))
r = int(input('Digite a razao dessa PA: '))

print('\nLogo a seguir estao os 10 priemiros termos dessa PA: ')
for pa in range(pt, r * 10, r):
    print(pa)
print('...')