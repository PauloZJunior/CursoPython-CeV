v = list()
while True:
    v.append(int(input('Digite um valor: ')))
    r = str(input('Deseja adicionar mais um número? [S/N]: ')).lower().strip().split()[0]
    while r not in 'sn':
        r = str(input('Deseja adicionar mais um número? [S/N]: ')).lower().strip().split()[0]
    if r == 'n':
        break
print('=-'*30)
q = len(v)
print(f'Foram digitados {q} números!')
v.sort(reverse=True)
print(f'A lista em ordem decrescente é: {v}')
if 5 in v:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')
