from time import sleep
print('='*30, 'BANCO DA NAY', '='*30, '\n')
s = c = v = d = u = t = l = 0
while True:
    e = 0
    print('O que você deseja fazer?')
    print('-='*37)
    while e not in range(1, 5):
        print('[1] SALDO\n[2] SAQUE\n[3] DEPOSITAR\n[4] SAIR')
        print('-=' * 37)
        e = int(input('Digite o número da sua escolha: '))
    if e == 1:
        print(f'Seu saldo é de: R${s:.2f}')
        print('-=' * 37)
    elif e == 2:
        if s <= 0:
            print('Você não tem saldo na sua conta!')
        else:
            vs = int(input('Qual valor você deseja sacar? '))
            if vs > s:
                print('Saldo insuficiente! Tente novamente mais tarde!')
            else:
                s -= vs
                print(f'Você está sacando R${vs:.2f}')
                c = vs // 50 #c recebe divisão inteira do saque por 50
                print(f'Total de {c} cédulas de R$50')
                t = c * 50 #t recebe divisão inteira de 50 vezes 50
                l = vs - t #l recebe valor do saque menos valor do t
                vs = l
                c = l // 20 # c recebe divisão inteira do restante do valor por 20
                print(f'Total de {c} cédulas de R$20')
                t = c * 20 # t recebe divisão inteira do resto do valor vezes 20
                l = vs - t
                vs = l
                c = l // 10
                print(f'Total de {c} cédulas de R$10')
                t = c * 10
                l = vs - t
                vs = l
                c = l // 1
                print(f'Total de {c} cédulas de R$1')
                print('='*30)
    elif e == 3:
        d = int(input('Qual o valor do depósito? R$'))
        s += d
    elif e == 4:
        print('SAINDO DO PROGRAMA... VOLTE SEMPRE!')
        sleep(2)
        break
print('='*35, 'FIM', '='*35)