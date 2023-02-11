2
from random import randint
from time import sleep
mega = list()
jogo = list()
print('-' * 50)
print(f"{'JOGOS DA MEGA SENA':>32}")
print('-' * 50)
r = int(input('Quantos jogos você deseja sortear? '))
for c in range(r):
    for j in range(0, 6):
        while True:
            n = randint(1, 60)
            if n not in jogo:
                jogo.append(n)
                break
    jogo.sort()
    mega.append(jogo[:])
    jogo.clear()
print('=-' * 5, end='')
print(f'SORTEANDO {r} JOGOS', end='')
print('=-' * 5)
for c in range(len(mega)):
    print(f'Jogo {c + 1}: {mega[c]}')
    sleep(1)
print('=-' * 5, end='')
print('BOA SORTE!', end='')
print('=-' * 5)
