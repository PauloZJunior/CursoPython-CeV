mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        mat[l][c] = int(input(f'Digite um valor para: [{l}, {c}]: '))
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{mat[l][c]:^5}]', end='')
    print()
