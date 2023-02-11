n = list()
c = 0
while True:
    nn = int(input('Digite um valor: '))
    if nn not in n:
        n.append(nn)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Deseja adicionar mais um número ? [S/N]')).lower().strip().split()[0]
    while r not in 'sn':
        r = str(input('Deseja adicionar mais um número ? [S/N]')).lower().strip().split()[0]
    if r == 'n':
        break
n.sort()
print('-='*50)
print(f'Você digitou os valores {n}')