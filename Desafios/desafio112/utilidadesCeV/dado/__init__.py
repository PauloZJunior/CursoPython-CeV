def leiaDinheiro(msg):
    valido = False
    while not valido:
        m = str(input(msg)).replace(',', '.').strip()
        if m.isalpha() or m == '':
            print(f'\033[1;31mERRO: "{m}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(m)






