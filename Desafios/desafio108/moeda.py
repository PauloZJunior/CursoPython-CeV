def dobro(n=0):
    return n * 2


def metade(n=0):
    return n / 2


def aumentar(n=0, a=0):
    return n + (a / 100 * n)


def diminuir(n=0, d=0):
    return n - (d / 100 * n)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')
    #v = str(f'R${n:.2f}').replace(".", ",")
    #return v

