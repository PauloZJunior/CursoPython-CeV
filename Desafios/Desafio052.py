n = int(input('Digite um número: '))
con = 0
if n <= 1 or n > 2 and n % 2 == 0:
    print(f'{n} - NÃO É PRIMO!')
    exit()
else:
    for c in range(n-1, 2, -1):
        if n % c == 0:
            con += 1
    if con == 0:
        print(f'{n} - É PRIMO!')
    else:
        print(f'{n} - NÃO É PRIMO!')
