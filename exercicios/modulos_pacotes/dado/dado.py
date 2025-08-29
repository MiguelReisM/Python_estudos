def leiaDinheiro(msg):
    while True:
        num = input('Digite um preco: R$').strip().replace(',','.')
        try:
            return float(num)
        except:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')