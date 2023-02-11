mat = [], [], []
s = tc = m = 0
for l in range(0, 3):
    for c in range(0, 3):
        v = int(input(f'Digite um valor para [{l}, {c}]: '))
        mat[l].append(v)
        if v % 2 == 0:
            s += v
        if l == 1:
            if m < v:
                m = v
        if c == 2:
            tc += v
print('=-' * 30)
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{mat[c][l]:^5}]', end='')
    print()
print('=-' * 30)
print(f'A soma de todos os pares é: {s}')
print(f'A soma dos valores da terceira coluna é: {tc}')
print(f'O maior valor da segunda linha é: {m}')
