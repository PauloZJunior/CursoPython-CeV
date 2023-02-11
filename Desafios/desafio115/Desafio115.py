import cadastro

cad = open("cadastro.txt", "a")
op = 0
val = False
while not val:
    try:
        print('-' * 50)
        print('MENU PRINCIPAL'.center(50))
        print('-' * 50)
        print('\033[1;33m1\033[m - \033[1;34mVer pessoas cadastradas\033[m')
        print('\033[1;33m2\033[m - \033[1;34mCadastrar nova pessoa\033[m')
        print('\033[1;33m3\033[m - \033[1;34mSair do sistema\033[m')
        print('-' * 50)
        op = cadastro.valop('\033[0;33mSua opção:\033[m')
    except:
        print('ERRO: Digite o número da opção desejada!')
    if op not in range(1, 4):
        print('\033[1;31mOpção inválida!\033[m')
    elif op == 1:
        cad = open("cadastro.txt", "r")
        print('-' * 50)
        print('PESSOAS CADASTRADAS'.center(50))
        print('-' * 50)
        print(cad.read())
        cad.close()
    elif op == 2:
        cad = open("cadastro.txt", "a")
        print('-' * 50)
        print('NOVO CADASTRO'.center(50))
        print('-' * 50)
        n = cadastro.nome('Nome:')
        i = cadastro.idade('Idade:')
        cad.write(f'{n: <40}')
        cad.write(f'{i: >3} anos')
        cad.write('\n')
        cad.close()
        print(f'Novo registro de {n} adicionado!')
        print('-' * 50)
    elif op == 3:
        print('-' * 50)
        print('SAINDO DO SISTEMA...ATÉ LOGO!'.center(50))
        print('-' * 50)
        break
