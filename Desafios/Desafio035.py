r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 + r2 > r3:
    if r1 + r3 > r2:
        if r3 + r2 > r1:
            print('Com essas medidas é possível formar um triângulo!')
        else:
            print('Com essas medidas NÃO é possível formar um triângulo!')
    else:
        print('Com essas medidas NÃO é possível formar um triângulo!')
else:
    print('Com essas medidas NÃO é possível formar um triângulo!')
