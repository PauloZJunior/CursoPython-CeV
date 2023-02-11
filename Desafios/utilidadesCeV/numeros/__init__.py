def leiaInt(n=0):
    val = False
    while not val:
        try:
            num = int(input(n))
        except(ValueError, TypeError):
            print('\033[1;31mERRO: Digite um número Inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário não informou o valor.\033[m')
            num = 0
            return num
        else:
            val = True
            return num


def leiaFloat(n=0):
    val = False
    while not val:
        try:
            num = float(input(n))
        except(ValueError, TypeError):
            print('\033[1;31mERRO: Digite um número Real válido!\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mO usuário não informou o valor.\033[m')
            num = 0
            return num
        else:
            val = True
            return num
