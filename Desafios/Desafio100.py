from random import randint
from time import sleep
numeros = list()


def sorteia():
    print('Sorteando 5 valores da lista: ', end=' ')
    for c in range(0, 5):
        numeros.append(randint(0, 10))
        print(f'{numeros[c]}', end='  ')
        sleep(0.5)
    print(' PRONTO!')


def somapar():
    sp = 0
    for c in range(0, 5):
        if numeros[c] % 2 == 0:
            sp += numeros[c]
    print(f'A soma dos valores pares é: {sp}')


sorteia()
somapar()
