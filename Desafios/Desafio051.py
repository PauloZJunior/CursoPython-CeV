'''t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
con = 0
print('Os 10 primeiros termos dessa PA é: ')
for c in range(0, 10):
    con = con + 1
for d in range(t, con*r, r):
    print(f'[{d}]')'''

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = pt + (10 - 1) * r
print('Os 10 primeiros termos dessa PA é: ')
for c in range(pt, decimo + r, r):
    print(f'[{c}]')
