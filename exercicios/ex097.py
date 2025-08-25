#Crie um programa que tenha uma funcao chamada escreva(), que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel.
def escreva(msg):
    print('=' * len(msg))
    print(msg)
    print('=' * len(msg))

msg1 = ' Bom dia mundo! '
msg2 = ' Boa tarde mundo! '
msg3 = ' Boa noite mundo, durmam bem! '
escreva(msg1)
escreva(msg2)
escreva(msg3)