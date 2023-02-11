pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
count = 0
pa = pt
print('Os 10 primeiros termos dessa PA é:')
while count < 10:
    print(f'  {pa}', end='')
    pa = pa + r
    count = count + 1
