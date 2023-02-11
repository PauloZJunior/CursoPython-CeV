num = count = s = 0
num = int(input('Digite um número [999] para parar: '))
while num != 999:
    s += num
    count += 1
    num = int(input('Digite um número [999] para parar: '))
print(f'Foram digitados {count} números e a soma entre eles é: {s}')
