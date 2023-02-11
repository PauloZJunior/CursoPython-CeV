print('='*30, 'CADASTRO DE PESSOAS', '='*30)
maior = h = mm = 0
while True:
    s = p = 'y'
    i = int(input('Digite a idade da pessoa: '))
    while s not in 'mf':
        s = str(input('Digite o sexo da pessoa [M/F]: ')).strip()[0].lower()
    if i > 18:
        maior += 1
    if s == 'm':
        h += 1
    if i < 20 and s == 'f':
        mm += 1
    while p not in 'sn':
        p = str(input('Você deseja continuar? [S/N]')).strip()[0].lower()
    if p == 'n':
        break
print('='*30, 'FIM DO PROGRAMA', '='*30)
print(f'Tem {maior} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {h} homens.')
print(f'Tem {mm} mulheres com menos de 20 anos.')
