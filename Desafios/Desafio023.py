'''NÃO FUNCIONA COM NÚMEROS COM MENOS DE 4 DÍGITOS'''
#n = str(input('Digite um número entre 0 até 9999: '))
#print(f'O número digitado foi: {n},\nSua unidade é: {n[3]}\nSua dezena é: {n[2]}\nSua centena é: {n[1]}\nSeu milhar é: {n[0]}')

'''FUNCIONA COM QUALQUER NÚMERO'''

n = int(input('Digite um número entre 0 até 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'O número digitado foi: {n}')
print(f'A unidade é: {u}')
print(f'A dezena é: {d}')
print(f'A centena é: {c}')
print(f'O milhar é: {m}')
