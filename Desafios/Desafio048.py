s = 0
for c in range(1, 501):
    m = c * 3
    rd = m % 2
    if m <= 500:
        if rd == 1:
            s += m
print(f'A soma de todos os valores é: {s}')
            