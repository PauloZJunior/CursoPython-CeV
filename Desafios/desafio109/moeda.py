def dobro(n=0, sit=False):
    '''
    -> Função para calcular o dobro de um número.
    :param n: número a ser calculado.
    :param sit: (opcional) se verdadeiro, formata o resultado em moeda.
    :return: retorna o resultado formatado ou não, de acordo com o :param sit
    '''
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

