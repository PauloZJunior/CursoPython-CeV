from random import randint
from time import sleep
print('\n')
print('\033[36m-=-' * 20)
print('\033[36m   Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n = int(input('\033[mEm que número eu pensei? '))
r = randint(0, 5)
print('\n')
print('\033[1;34m-#-' * 15)
print('                \033[1;34mPROCESSANDO...')
print('-#-' * 15)
print('\n')
sleep(3)
if n == r:
    print('\n\033[1;32mPARABÉNS, VOCÊ ACERTOU !!!')
else:
    print(f'\n\033[1;31mVOCÊ PERDEU !!! Eu pensei no número {r}.')
