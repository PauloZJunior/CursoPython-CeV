from time import sleep

c = ('\033[m',  # 0 - SEM COR
     '\033[7;40m',  # 1 - BRANCO
     '\033[1;30;41m',  # 2 - VERMELHO
     '\033[1;30;42m',  # 3 - VERDE
     '\033[1;30;43m',  # 4 - AMARELO
     '\033[1;30;44m',  # 5 - AZUL
     '\033[1;30;45m',  # 6 - MAGENTA
     '\033[1;30;46m',  # 7 - CIANO
     '\033[1;30;47m',  # 8 - CINZA
     )


def ajuda():
    print(c[1], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# programa principal
com = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 4)
    com = str(input('Função ou Biblioteca > '))
    if com.upper() == 'FIM':
        break
    else:
        titulo(f'EXIBINDO MANUAL DO COMANDO ({com})', 5)
        ajuda()
titulo('ATÉ LOGO', 2)
sleep(1)
