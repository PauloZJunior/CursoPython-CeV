from datetime import date
d = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    i = int(input(f'Digite o ano de nascimento da {c}º pessoa: '))
    if d - i < 21:
        menor = menor + 1
    else:
        maior = maior + 1
print('Considerando a maioridade com 21 anos:')
print(f'{maior} pessoas são maiores de idade!')
print(f'{menor} pessoas são menores de idade!')