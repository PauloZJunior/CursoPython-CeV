sp = 0
si = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    rd = n % 2
    if rd == 0:
        sp = sp + n
    else:
        si = si + n
print(f'A soma dos números pares é: {sp}')
print(f'A soma dos números ímpares é: {si}')
