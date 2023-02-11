import sys


def valop(n=0):
    val = False
    while not val:
        try:
            n = int(input('\033[1;33mSua Opção: \033[m'))
        except (ValueError, TypeError):
            print('\033[1;31mValor inválido!\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mNão foi digitado nenhuma opção!\033[m')
            n = 3
            val = True
            return n
        else:
            val = True
            return n


def idade(n=0):
    val = False
    while not val:
        try:
            n = int(input('Idade: '))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: Por favor, digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mNão foi informado a idade!\033[m')
            print('-' * 50)
            print('ENCERRANDO O PROGRAMA'.center(50))
            print('-' * 50)
            sys.exit()
        else:
            val = True
            return n


def nome(msg='<desconhecido>'):
    val = False
    while not val:
        try:
            n = str(input('Nome: '))
            if not n.strip().replace(" ", "").isalpha():
                raise Exception
        except(ValueError, TypeError):
            print('\033[1;31mNome inválido!\033[m')
        except Exception:
            print('\033[1;31mNome inválido!\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mNão foi informado o nome!\033[m')
            print('-' * 50)
            print('ENCERRANDO O PROGRAMA'.center(50))
            print('-' * 50)
            sys.exit()
        else:
            val = True
            return n