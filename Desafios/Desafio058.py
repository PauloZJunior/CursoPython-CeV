from random import randint
r = str(input('Vamos jogar? [S/N]')).lower()[0].strip()
print('='*20, 'VOU PENSAR EM UM NÚMERO DE 0 A 10, TENTE ADIVINHAR QUAL !', '='*20)
c = randint(0, 10)
while r in 's':
    u = int(input('Qual número eu pensei? '))
    if u not in range(0, 10):
        print('Valor inválido, Informe um número de 0 a 10.')
    else:
        t = 0
        if c == u:
            print('PARABÉNS !!! VOCÊ ACERTOU DE PRIMEIRA!')
            print('=' * 100)
            r = str(input('Deseja jogar novamente? [s/n]: ')).lower()[0].strip()
            if r == 'n':
                exit()
        while c != u:
            print('ERROU ! TENTE NOVAMENTE')
            u = int(input('Qual número eu pensei? '))
            t += 1
        print(f'ACERTOU !!! Você precisou de {t+1} tentativas para acertar !')
        print('='*100)
        r = str(input('Deseja jogar novamente? [s/n]: ')).lower()
