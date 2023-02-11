num = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'Os números pares foram: {num[0]}')
print(f'Os números ímpares foram: {num[1]}')
