def moeda(n, simbolo="R$"):
    # Formata o valor em moeda brasileira
    return f'{simbolo}{n:.2f}'.replace('.', ',')


def aumentar(n, taxa=10, formatar=False):
    # Aumenta o valor em X%
    res = n + (n * taxa / 100)
    return moeda(res) if formatar else res


def diminuir(n, taxa=13, formatar=False):
    # Diminui o valor em X%
    res = n - (n * taxa / 100)
    return moeda(res) if formatar else res


def dobro(n, formatar=False):
    # Dobra o valor
    res = n * 2
    return moeda(res) if formatar else res


def metade(n, formatar=False):
    # Metade do valor
    res = n / 2
    return moeda(res) if formatar else res
