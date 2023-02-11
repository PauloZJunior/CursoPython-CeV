from time import sleep
jogador = dict()
gols = list()
dados = list()
while True:
    g = 0
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for e in range(1, p + 1):
        gols.append(int(input(f'Quantos gols na {e}ª partida? ')))
        g += gols[e - 1]
    jogador['gols'] = gols[:]
    jogador['total'] = g
    dados.append(jogador.copy())
    while True:
        r = str(input('Quer continuar? [S/N]: ')).split()[0].strip().lower()
        if r in 'sn':
            break
        print('*****ERRO! Por favor, digite apenas S ou N.*****')
    if r == 'n':
        break
print('=-' * 50)
print(dados)
print('=-' * 50)
print(f'{"cod":<6}{"nome":<35}{"gols":<35}{"total"}')
print('-' * 100)
for k, v in enumerate(dados):
    print(f'{k:<6}', end='')
    for d in v.values():
        print(f'{str(d):<35}', end='')
    print()
print('=-' * 50)
while True:
    r = int(input('Digite o código do jogador para mostrar seus dados(999 para parar): '))
    if r == 999:
        print('ENCERRANDO...')
        sleep(1)
        print('VOLTE SEMPRE!')
        break
    if r in range(len(dados)):
        print('-' * 100)
        print(f'--LEVANTAMENTO DO JOGADOR {dados[r]["nome"].upper()}--')
        print('-' * 100)
        for c in range(0, len(dados[r]["gols"])):
            print(f'No jogo {c + 1} fez {dados[r]["gols"][c]} gols.')
        print(f'O jogador {dados[r]["nome"]} fez {dados[r]["total"]} gols em toda temporada!')
        print('-' * 100)
    else:
        print('VALOR INVÁLIDO! TENTE NOVAMENTE!')
