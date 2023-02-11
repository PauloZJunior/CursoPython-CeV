from time import sleep
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2) / 2
print(f'Sua média foi {m:.1f}. Portanto você foi...')
sleep(1)
if m < 5:
    print('\033[31mREPROVADO!!!\033[m')
elif m < 7:
    print('\033[33mRECUPERAÇÃO!!!\033[m')
else:
    print('\033[32mAPROVADO!!!\033[m')
