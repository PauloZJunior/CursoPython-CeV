from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = hypot(co, ca)
print(f'Sendo o cateto oposto {co} e o cateto adjacente {ca} a hipotenusa é: {h:.2f}')
