f = str(input('Digite uma frase: ')).strip().lower().split()
f = (''.join(f))
con = len(f)
i = 0
for c in range(0, con):
    con = con - 1
    if f[c] == f[con]:
        i = i + 1
    else:
        print('NÃO É PALÍNDROMO')
        exit()
print('É PALÍNDROMO')
