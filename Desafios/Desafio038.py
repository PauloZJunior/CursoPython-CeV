n1 = int(input('Digite o 1º valor inteiro: '))
n2 = int(input('Digite o 2º valor inteiro: '))
if n1 > n2:
    print('O primeiro valor é o \033[34mMAIOR\033[m!!!')
    print('O segundo valor é o \033[31mMENOR\033[m!!!')
elif n2 > n1:
    print('O primeiro valor é o \033[31mMENOR\033[m!!!')
    print('O segundo valor é o \033[34mMAIOR\033[m!!!')
else:
    print('Os dois valores são \033[32mIGUAIS\033[m!!!')
