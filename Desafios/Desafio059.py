n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))
e = 0
while e != 5:
    print('-' * 26, 'O que você deseja fazer ?', '-' * 40)
    print('='*100)
    print(' ')
    print(' '*25, '[1] - SOMAR OS NÚMEROS')
    print(' '*25, '[2] - MULTIPLICAR OS NÚMEROS')
    print(' '*25, '[3] - SABER O MAIOR VALOR')
    print(' '*25, '[4] - DIGITAR NOVOS NÚMEROS')
    print(' '*25, '[5] - SAIR DO PROGRAMA')
    print(' ')
    print('='*100)
    e = int(input('Digite o número da opção correspondente: '))
    print('=' * 100)
    if e == 1:
        print(f'A soma entre {n1} + {n2} é: {n1 + n2:.1f}\n')
    elif e == 2:
        print(f'A multiplicação entre {n1} e {n2} é: {n1*n2:.1f}\n')
    elif e == 3:
        if n1 > n2:
            print(f'O maior número é: {n1}\n')
        elif n2 > n1:
            print(f'O maior número é: {n2}\n')
        else:
            print('Os dois números são iguais!\n')
    elif e == 4:
        n1 = float(input('Digite o 1º valor: '))
        n2 = float(input('Digite o 2º valor: '))
        print(' ')
    elif e == 5:
        exit()
    else:
        print(' '*30, 'VALOR INVÁLIDO !\n')
