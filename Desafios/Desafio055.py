for c in range(1, 6):
    p = float(input(f'Digite o peso da {c}º pessoa: '))
    if c == 1:
        maior = p
        menor = p
    elif p > maior:
        maior = p
    elif p < menor:
        menor = p
print(f'O maior peso é: {maior}Kg.')
print(f'O menor peso é: {menor}Kg.')
