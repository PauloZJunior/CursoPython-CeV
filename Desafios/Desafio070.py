print('='*30, 'LOJA DA NAY', '='*30)
t = pmc = pmb = 0
nmb = 'y'
while True:
    res = 'y'
    n = str(input('Digite o nome do produto: '))
    p = float(input('Qual o valor do produto? R$'))
    t += p
    if pmb == 0 or pmb > p:
        pmb = p
        nmb = n
    if p > 1000:
        pmc += 1
    while res not in 'sn':
        res = str(input('Quer continuar? [S/N] ')).strip()[0].lower()
    if res == 'n':
        break
print('='*30, 'FIM DO PROGRAMA', '='*30)
print(f'O total da compra foi R${t:.2f}')
print(f'Temos {pmc} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nmb} que custa R${pmb}')
