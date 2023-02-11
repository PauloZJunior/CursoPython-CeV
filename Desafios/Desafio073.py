times = ('Corinthians', 'Bragantino', 'Atlético-MG', 'Santos', 'Coritiba', 'Cuiabá', 'Internacional', 'Avaí', 'América-MG',
         'Palmeiras', 'Flamengo', 'Botafogo', 'São Paulo', 'Fluminense', 'Ceará SC', 'Athletico-PR', 'Atlético-GO',
         'Goiás', 'Juventude', 'Fortaleza')
print('*'*30, 'CLASSIFICAÇÃO BRASILEIRÃO 2022', '*'*30)
print(f'\nOs 5 Primeiros colocados são: {times[0:5]}')
print(f'Os últimos 4 colocados são: {times[-4:]}')
print(f'Em ordem alfabética a lista fica: ', sorted(times))
print(f'O fluminense está na {times.index("Fluminense")+ 1}ª posição!')



'''for c in range(len(times)):
    if times[c] in 'Fluminense':
        print(f'Fluminense está na {c+1}ª posição')
    if c == range(len(times)):
        print(f'Fluminense não está em nenhuma posição!')'''

