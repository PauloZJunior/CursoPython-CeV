while True:
    print(f'=' * 50)
    n = int(input('Deseja ver a tabuada de qual valor? '))
    if n < 0:
        break
    print(f'='*50)
    for c in range(1, 11):
        print(f'{n} x {c} = {c*n}')
print('Programa Tabuada Encerrado !')