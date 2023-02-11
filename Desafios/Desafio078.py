n = list()
maior = menor = 0
for c in range(0, 5):
    n.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = n[c]
    else:
        if n[c] > maior:
            maior = n[c]
        if n[c] < menor:
            menor = n[c]
print('=-' * 30)
print(f'Você digitou os valores {n}')
print(f'O maior valor é {maior} e ele está nas posições ', end='')
for i, v in enumerate(n):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor é {menor} e ele está nas posições ', end='')
for i, v in enumerate(n):
    if v == menor:
        print(f'{i}... ', end='')
