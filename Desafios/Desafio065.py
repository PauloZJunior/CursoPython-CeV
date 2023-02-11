r = 's'
count = s = 0
while r == 's':
    n = int(input('Digite um número: '))
    if count == 0:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    count += 1
    s += n
    r = str(input('Quer continuar? [S/N]:')).lower().strip()[0]
print(f'Você digitou {count} valores e a média deles é: {s/count:.2f}')
print(f'O maior valor foi: {maior}\nO menor valor foi: {menor}')
