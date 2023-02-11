a = int(input('Digite um ano para saber se ele é bissexto ou não: '))
r = a % 4
r2 = a % 100
r3 = a % 400
if r == 0:
    if r2 == 0:
        if r3 == 0:
            print(f'O ano {a} é um ano bissexto!')
        else:
            print(f'O ano {a} não é um ano bissexto!')
    else:
        print(f'O ano {a} é um ano bissexto!')
else:
    print(f'O ano {a} não é bissexto!')
