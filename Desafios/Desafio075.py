n = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'O número 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3) + 1}ª posição.')
else:
    print('O valor 3 não apareceu em nenhuma posição!')
print(f'Os números pares foram: ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')
