n = list()
p = list()
i = list()
while True:
    n.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N]: ')).lower().strip().split()[0]
    while r not in 'sn':
        r = str(input('Quer continuar? [S/N]: ')).lower().strip().split()[0]
    if r == 'n':
        break
print('=-' * 30)
t = len(n)
for c in range(t):
    if n[c] % 2 == 0:
        p.append(n[c])
    else:
        i.append(n[c])
print(f'A lista completa é: {n}.')
print(f'A lista de pares é: {p}.')
print(f'A lista de ímpares é: {i}.')
