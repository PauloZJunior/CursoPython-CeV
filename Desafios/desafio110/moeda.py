def dobro(n=0, sit=False):
    res = n * 2
    return res if sit is False else moeda(res)


def metade(n=0, sit=False):
    res = n / 2
    return res if sit is False else moeda(res)


def aumentar(n=0, a=0, sit=False):
    res = n + (a / 100 * n)
    return res if sit is False else moeda(res)


def diminuir(n=0, d=0, sit=False):
    res = n - (d / 100 * n)
    return res if sit is False else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, v1=0, v2=0):
     print('-' * 30)
     print('RESUMO DO VALOR'.center(30))
     print('-' * 30)
     print(f'Preço analisado: \t{moeda(n)}')
     print(f'Dobro do preço: \t{dobro(n, True)}')
     print(f'Metade do preço: \t{metade(n, True)}')
     print(f'{v1}% de aumento: \t{aumentar(n, v1, True)}')
     print(f'{v2}% de redução: \t{diminuir(n, v2, True)}')
     print('-' * 30)
