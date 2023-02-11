cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        else:
            print('NÚMERO INVÁLIDO! ', end='')
    print(f'O número digitado foi {cont[n]}')
    while True:
        r = str(input('Gostaria de digitar novamente? [S/N]: '.lower().strip()))
        if r not in 'sn':
            print('Resposta inválida!')
        else:
            break
    if r in 'n':
        break
