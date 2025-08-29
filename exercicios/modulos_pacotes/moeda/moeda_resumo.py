def moeda(n, simbolo="R$"):
    # Formata o valor em moeda brasileira
    return f'{simbolo}{n:.2f}'.replace('.', ',')


def aumentar(n, taxa=10):
    # Aumenta o valor em X%
    res = n + (n * taxa / 100)
    return moeda(res)


def diminuir(n, taxa=13):
    # Diminui o valor em X%
    res = n - (n * taxa / 100)
    return moeda(res)


def dobro(n):
    # Dobra o valor
    res = n * 2
    return moeda(res)


def metade(n):
    # Metade do valor
    res = n / 2
    return moeda(res)


def resumo(n, taxa_au, taxa_di):
    print('=-' * 16)
    print(f'{"Resumo do valor!":^32}')
    print('=-' * 16)
    print(f'{"Preco analisado: ":<20}{moeda(n):>5}')
    print(f'{"Dobro do preco: ":<20}{dobro(n):>5}')
    print(f'{"Metade do preco: ":<20}{metade(n):>5}')
    print(f'{taxa_au}% de aumento:'.ljust(20) + f'{aumentar(n, taxa_au)}')
    print(f'{taxa_di}% de redução:'.ljust(20) + f'{diminuir(n, taxa_di)}')
    print('=-' * 16)
