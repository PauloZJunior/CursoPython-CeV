pessoas = list()
dados = list()
p = maipe = menpe = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Deseja continuar? [S/N] ')).strip().lower().split()[0]
    p += 1
    print('=-' * 30)
    if r == 'n':
        break
for j in pessoas:
    if j[1] > maipe:
        maipe = j[1]
for j in pessoas:
    if menpe == 0:
        menpe = j[1]
    else:
        if j[1] < menpe:
            menpe = j[1]
print(f'Foram cadastradas {p} pessoas.')
print(f'O maior peso foi: {maipe}Kg, e foi o peso de: ', end='')
for i, v in enumerate(pessoas):
    if v[1] == maipe:
        print(f'{v[0]}...', end='')
print()
print(f'O menor peso foi: {menpe}Kg, e foi o peso de: ',end='')
for i, v in enumerate(pessoas):
    if v[1] == menpe:
        print(f'{v[0]}...', end='')
