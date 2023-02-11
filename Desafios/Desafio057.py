'''f = 'f'
m = 'm'
s = ''
while s != f and s != m:
    s = str(input('Informe o sexo da pessoa: [M/F] ')).lower()[0].strip()
    if s != f and s != m:
        print('Valor inválido!')
        print('-='*20)
print('Validado com sucesso!')'''
s = str(input('Informe seu sexo [M/F]: ')).lower()[0].strip()
while s not in 'mf':
    print('Dados inválidos!!! Tente novamente!')
    s = str(input('Informe seu sexo [M/F]: ')).lower()[0].strip()
print(f'Sexo {s} validado com sucesso!')