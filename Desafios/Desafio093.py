jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for e in range(0, p):
    gols.append(int(input(f'Quantos gols na {e + 1}ª partida? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)#comando sum soma tudo que tem em gols
print('-=' * 50)
print(jogador)
print('-=' * 50)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 50)
print(f'O jogador {jogador["nome"]} jogou {p} partidas.')
for c in range(1, p + 1):
    print(f'Na partida {c}, ele fez {gols[c - 1]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
