n = int(input('Digite um número inteiro para ser convertido: '))
e = int(input('Digite [1] para binário\nDigite [2] para octal\nDigite [3] para hexadecimal\nDigite aqui sua escolha: '))
a = 1
b = 2
c = 3
if e == a:
    print(f'A conversão de {n} em decimal, fica {bin(n)[2:]} em binário.')
elif e == b:
    print(f'A conversão de {n} em decimal, fica {oct(n)[2:]} em octal.')
elif e == c:
    print(f'A conversão de {n} em decimal fica {hex(n)[2:]} em hexadecimal.')
else:
    print('Você não digitou um valor válido!!!')
