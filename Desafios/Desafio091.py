from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
ranking = dict()
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)
    print(f'Jogador {c} tirou:', jogadores[f'jogador{c}'], 'no dado.')
    sleep(0.8)
print('-=' * 50)
print('== RANKING DOS JOGADORES ==')
print('-=' * 50)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for c in range(1, 5):
    print(f'{c}º lugar: {ranking[c - 1][0]} que tirou {ranking[c - 1][1]}')
    sleep(0.8)
