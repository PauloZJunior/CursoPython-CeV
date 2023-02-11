e = int(input('Quantos elementos da sequência de Fibonacci você deseja? '))
count = 1
n0 = 0
n1 = 1
f = 1
while count < e:
    if count == 1:
        print('0 → ', end='')
    print(f'{f} → ', end='')
    f = n0 + n1
    n0 = n1
    n1 = f
    count += 1

