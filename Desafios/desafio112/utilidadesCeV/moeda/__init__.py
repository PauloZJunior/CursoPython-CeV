def dobro(n, sit=False):
    res = n * 2
    return res if sit is False else moeda(res)


def metade(n, sit=False):
    res = n / 2
    return res if sit is False else moeda(res)


def aumentar(n, a, sit=False):
    res = n + (a / 100 * n)
    return res if sit is False else moeda(res)


def diminuir(n, d, sit=False):
    res = n - (d / 100 * n)
    return res if sit is False else moeda(res)


def moeda(n):
    v = str(f'R${n:.2f}').replace(".", ",")
    return v


def resumo(n, v1, v2):
     print('-' * 30)
     print('RESUMO DO VALOR'.center(30))
     print('-' * 30)
     print(f'Preço analisado:\t{moeda(n)}')
     print(f'Dobro do preço:\t\t{dobro(n, True)}')
     print(f'Metade do preço:\t{metade(n, True)}')
     print(f'{v1}% de aumento:\t\t{aumentar(n, v1, True)}')
     print(f'{v2}% de redução:\t\t{diminuir(n, v2, True)}')
     print('-' * 30)
