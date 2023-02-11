pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))
count = 0
pa = pt
print('Os 10 primeiros termos dessa PA é: ')
while count < 10:
    print(f'  {pa}', end='')
    pa += r
    count += 1
print(' ')
tam = 1
while tam != 0:
    tam = int(input('\nQuantos termos a mais você deseja ver? Digite 0 para encerrar!'))
    if tam == 0:
        exit()
    count = 0
    print(f'Os próximos {tam} termos dessa PA é:')
    while count < tam:
        print(f'  {pa}', end='')
        pa += r
        count += 1
