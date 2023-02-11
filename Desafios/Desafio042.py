r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 + r2 > r3:
    if r2 + r3 > r1:
        if r1 + r3 > r2:
            print('Com essas três medidas é \033[32mPOSSÍVEL\033[m formar um triângulo.')
            if r1 == r2 and r1 == r3:
                print(f'Com as medidas {r1}, {r2} e {r3}, é possível formar um triângulo equilátero.')
            elif r1 != r2 and r1 != r3 and r2 != r3:
                print(f'Com as medidas {r1}, {r2}, e {r3}, é possível formar um triângulo escaleno.')
            elif r1 == r2 or r1 == r3 or r2 == r3:
                print(f'Com as medidas {r1}, {r2}, e {r3}, é possível formar um triângulo isósceles.')
        else:
            print('Com essas três medidas é \033[31mIMPOSSÍVEL\033[m formar um triângulo.')
    else:
        print('Com essas três medidas é \033[31mIMPOSSÍVEL\033[m formar um triângulo.')
else:
    print('Com essas três medidas é \033[31mIMPOSSÍVEL\033[m formar um triângulo.')
