dados = list()
cad = dict()
m = list()
pam = list()
si = 0
while True:
    cad['nome'] = str(input('Nome: '))
    while True:
        cad['sexo'] = str(input('Sexo[M/F]: ')).strip().split()[0].lower()
        if cad['sexo'] in 'mf':
            break
        print('*****ERRO! Por favor, digite apenas M ou F.*****')
    cad['idade'] = int(input('Idade: '))
    dados.append(cad.copy())
    cad.clear()
    while True:
        r = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).strip().split()[0].lower()
        if r in 'sn':
            break
        print('*****ERRO! Por favor, digite apenas S ou N.*****')
    if r in 'n':
        break
for c in range(len(dados)):
    si += dados[c]['idade']
    if dados[c]['sexo'] in 'f':
        m.append(dados[c]['nome'])
print(f'A) Foram cadastradas {len(dados)} pessoas.')
print(f'B) A média de idade do grupo é: {si/len(dados)} anos.')
print(f'C) As mulheres do grupo são: {m}')
for c in range(len(dados)):
    if dados[c]['idade'] > si/len(dados):
        pam.append(dados[c]['nome'])
print(f'D) As pessoas com idade acima da média são: {pam}')