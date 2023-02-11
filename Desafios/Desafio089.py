#OUTRA MANEIRA DE FAZER
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]: ')).lower().strip().split()[0]
    if resp in 'n':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 encerra): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')



#MINHA MANEIRA DE FAZER
'''
lista = list()
nome = list()
notas = list()
m = 0
while True:
    nome.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    m = (notas[0] + notas[1]) / 2
    notas.append(m)
    nome.append(notas[:])
    lista.append(nome[:])
    nome.clear()
    notas.clear()
    r = str(input('Deseja continuar? [S/N]: ')).strip().lower().strip()[0]
    if r in 'n':
        break
print('=-' * 30)
print(f'{"Nº":<5}', f'{"NOME":<19}', f'{"MÉDIA":<20}')
print('-' * 60)
for c in range(len(lista)):
    print(f'{c:<6}', end='')
    print(f'{lista[c][0]:<20}', end='')
    print(f'{lista[c][1][2]:<20}')
print('-' * 60)
while True:
    r = int(input('Mostrar notas de qual aluno? (999 encerra o programa!): '))
    if r == 999:
        print('PROGRAMA ENCERRADO! VOLTE SEMPRE!')
        break
    elif r >= len(lista):
        print('Valor inválido, tente novamente!')
    else:
        print(f'Notas de {lista[r][0]} são: {lista[r][1][0:2]}')
        print('-' * 60)'''
