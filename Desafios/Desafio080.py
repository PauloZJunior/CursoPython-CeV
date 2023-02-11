n = list()
for c in range(0, 5):
    va = int(input('Digite um valor: '))
    if c == 0 or va > n[-1]:
        n.append(va)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(n):
            if va <= n[pos]:
                n.insert(pos, va)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados em ordem foram: {n}')