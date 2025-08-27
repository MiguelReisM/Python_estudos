#Crie um programa que tenha a funcao fatorial() que receba dois parametros: o primeiro que indique o numero a calcular e o outro chamado show, que sera um valor logico (opcional) indicando se sera mostrado ou nao na tela o processo de calculo fatorial
def fatorial(n, show=False):
    resultado = 1
    for i in range(n, 0, -1):
        resultado *= i
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return resultado


print(fatorial(5, show=True))
print(fatorial(5))