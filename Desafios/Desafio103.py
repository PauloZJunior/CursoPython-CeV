def ficha(j='<desconhecido>', go=0):
   print(f'O jogador {j} fez {go} gol(s) no campeonato.')


#programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(go=g)
else:
    ficha(n, g)
