def aumentar(n, taxa=10):
    # Aumenta o valor em X%
    return n + (n * taxa / 100)


def diminuir(n, taxa=13):
    # Diminui o valor em X%
    return n - (n * taxa / 100)


def dobro(n):
    # Dobra o valor
    return n * 2


def metade(n):
    # Metade do valor
    return n / 2


def moeda(n, simbolo="R$"):
    # Formata o valor em moeda brasileira
    return f'{simbolo}{n:.2f}'.replace('.', ',')