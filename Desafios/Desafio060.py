'''n = int(input('Digite um número: '))
r = n
for c in range(1, n):
    r = r * c
print(r)'''
n = int(input('Digite um número: '))
f = n
count = n - 1
while count > 0:
    f = f * count
    count = count - 1
print(f'O fatorial de {n} é {f}.')
