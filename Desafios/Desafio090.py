infor = dict()
infor['nome'] = str(input('Nome: '))
infor['média'] = float(input(f'Média de {infor["nome"]}: '))
if infor['média'] >= 7:
    infor['situação'] = 'APROVADO'
elif infor['média'] >= 5 < 7:
    infor['situação'] = 'RECUPERAÇÃO'
else:
    infor['situação'] = 'REPROVADO'
for k, v in infor.items():
    print(f' - {k}: {v}')
'''print(f'Nome é igual {infor["nome"]}')
print(f'Média é igual a {infor["média"]}')
print(f'Situação é igual a {infor["situação"]}')'''
