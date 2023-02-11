m = 0
fm = 0
mv = 0
nmv = 's'
for c in range(1, 5):
    n = str(input(f'Digite o nome da {c}º pessoa: '))
    i = int(input(f'Digite a idade da {c}º pessoa: '))
    s = str(input(f'Digite M ou F para o sexo da {c}º pessoa: ')).lower()
    print('-='*30)
    m += i
    if s == 'f' and i < 20:
        fm += 1
    if s == 'm' and i > mv:
        mv = i
        nmv = n
print(f'A média de idade do grupo é: {m/4:.1f} anos.')
print(f'{fm} mulheres tem menos de 20 anos de idade.')
print(f'O nome do homem mais velho é: {nmv} e ele tem {mv} anos.')
