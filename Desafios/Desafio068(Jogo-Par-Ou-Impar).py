from random import randint
print('=-'*20, 'JOGO DO PAR OU ÍMPAR', '=-'*20)
s = count = 0
r = 's'
while r in 's':
    while True:
        v = int(input('Diga um valor: '))
        e = ' '
        while e not in 'pi':
            e = str(input('PAR ou ÍMPAR? [P/I]: ')).strip()[0].lower()
        c = randint(0, 10)
        s = c + v
        if s % 2 == 0:
            if e == 'p':
                print('-'*80)
                print(f'ACERTOU!!! Você jogou {v} e o computador {c}. Total de {s} DEU PAR')
                print('-' * 80)
                count += 1
            else:
                print('-'*80)
                print(f' ERROU!!! Você jogou {v} e o computador {c}. Total de {s} DEU PAR')
                print('-' * 80)
                break
        else:
            if e == 'i':
                print('-'*80)
                print(f' ACERTOU!!! Você jogou {v} e o computador {c}. Total de {s} DEU ÍMPAR')
                print('-' * 80)
                count += 1
            else:
                print('-'*80)
                print(f'ERROU!!! Você jogou {v} e o computador {c}. Total de {s} DEU ÍMPAR')
                print('-' * 80)
                break
    print(f'GAME OVER! Você venceu {count} vezes.')
    r = str(input('Deseja jogar novamente? [S/N]')).lower().strip()[0]
print('FIM DO JOGO ! VOLTE SEMPRE!')
