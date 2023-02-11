from random import randint
na = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for c in na:
    print(f'{c}, ', end='')
print(f'\n O maior valor sorteado foi {max(na)}')
print(f'O menor valor sorteado foi: {min(na)}')





'''for c in range(0, 5):
    if c == 0:
        menor = na[0]
        maior = na[0]
    else:
        if na[c] > maior:
            maior = na[c]
        elif na[c] < menor:
            menor = na[c]
print(f'Os números gerados foram: {na}')
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')'''

