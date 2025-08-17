#Crie um programa que faca o computador jogar jokenpo com voce
import random
jokenpo = ['Pedra', 'Papel', 'Tesoura']
escolha_ususario = int(input('Digite qual opcao voce deseja:\n1 - Pedra\n2 - Papel\n3 - Tesoura\nOpcao desejada: '))
escolha_pc = random.choice(jokenpo)


if escolha_ususario == 1:
    print(f'Voce jogou Pedra e o computador {escolha_pc}')
    if escolha_pc == 'Tesoura':
        print('Parabens voce ganhou!')
    elif escolha_pc == 'Pedra':
        print('Tivemos um empate')
    else:
        print('Infelizmente voce perdeu')
elif escolha_ususario == 2:
    print(f'Voce jogou Papel e o computador {escolha_pc}')
    if escolha_pc == 'Pedra':
        print('Parabens voce ganhou!')
    elif escolha_pc == 'Papel':
        print('Tivemos um empate')
    else:
        print('Infelizmente voce perdeu')
elif escolha_ususario == 3:
    print(f'Voce jogou Tesoura e o computador {escolha_pc}')
    if escolha_pc == 'Papel':
        print('Parabens voce ganhou!')
    elif escolha_pc == 'Tesoura':
        print('Tivemos um empate')
    else:
        print('Infelizmente voce perdeu')
else:
    print('Escolha uma opcao valida!')