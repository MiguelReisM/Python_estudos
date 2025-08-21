#Crie um programa que leia a idade e o sexo de varias pessoas. Cada pessoa cadastrada, o programa deverá perguntar se o ususario quer ou nao continuar. No final mostre:
# quantas pessoas tem mais de 18 anos
# quantas mulheres tem menos de 20 anos
# quantos homens foram cadastrados
total_pessoas = homens = maiores_18 = mulheres_menos_20 = 0

print('-=' * 20)
while True:
    total_pessoas += 1
    idade = 0
    while idade <= 0:
        idade = int(input(f'Digite a idade da {total_pessoas}ª pessoa: '))
        if idade <= 0:
            print('Idade ivalida! Digite um numero valido.')

    sexo = ''
    while sexo not in ('m', 'f'):
        sexo = input('Digite o sexo (M/F): ').strip().lower()
        if sexo not in ('m', 'f'):
            print('OpOpcao ivalida! Digite M ou F.')

    if idade > 18:
        maiores_18 += 1
    if sexo == 'f' and idade < 20:
        mulheres_menos_20 += 1
    if sexo == 'm':
        homens += 1

    opcao = ''
    while opcao not in ('s', 'n'):
        opcao = input('\nDeseja continuar? (S/N): ').strip().lower()
        if opcao not in ('s', 'n'):
            print('Opcao ivalida! Digite S ou N.')
    print('-=' * 20)
    if opcao == 'n':
        break

print(f'Dentre a(s) {total_pessoas} pessoa(s) cadastrada(s):')
print(f'- {maiores_18} têm mais de 18 anos;')
print(f'- {mulheres_menos_20} mulher(es) têm menos de 20 anos;')
print(f'- {homens} homem(ns) foram cadastrados.')