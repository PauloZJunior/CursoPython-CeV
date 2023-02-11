def fatorial(num, show=False):
    """
    ->Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: retorna o valor do fatorial de num.
    """
    if show:
        print(f'{num}', end='')
        f = num
        for c in range(1, num):
            f = f * c
            print(f' x {num - c}', end='')
        print(f' = ', end='')
        return f
    else:
        f = num
        for c in range(1, num):
            f = f * c
        return f


#programa principal
print(fatorial(5, True))
help(fatorial)


#f = int(input('Digite um número para calcular o fatorial: '))
#r = str(input('Deseja mostrar o cálculo? [S/N]: ')).strip().lower().split()[0]
#if r == 's':
#    r = 1
#else:
#    r = 0
#fatorial(f, r)
