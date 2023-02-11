from time import sleep
from random import randint
import emoji
print('='*30)
print('   Vamos jogar Jokenpô...')
print('='*30)
print('\n1- Pedra', emoji.emojize('\U0001f44a\U0001f3fb'))
print('2- Papel', emoji.emojize(':hand_with_fingers_splayed:'))
print('3- Tesoura', emoji.emojize(':victory_hand:\n'))
print('='*30)
e = int(input('Digite aqui a sua escolha: '))
c = randint(1, 3)
if e < 1 or e > 3:
    print('JOGADA INVÁLIDA !!!')
    exit()
print('='*30)
print('-='*30)
print('                           JO')
sleep(1)
print('                           KEN')
sleep(1)
print('                           PÔ!!!')
sleep(1)
print('-='*30)
if e == 1 and c == 3:
    print('VOCÊ GANHOU !!!')
    print('Você escolheu pedra', emoji.emojize('\U0001f44a\U0001f3fb'), 'e eu escolhi tesoura.', emoji.emojize(':victory_hand:'))
elif e == 1 and c == 2:
    print('EU GANHEI !!!')
    print('eu escolhi papel.', emoji.emojize(':hand_with_fingers_splayed:'))
elif e == 1 and c == 1:
    print('EMPATOU !!!')
    print('eu também escolhi pedra', emoji.emojize('\U0001f44a\U0001f3fb'))
if e == 2 and c == 1:
    print('VOCÊ GANHOU !!!')
    print('eu escolhi pedra.', emoji.emojize('\U0001f44a\U0001f3fb'))
elif e == 2 and c == 3:
    print('EU GANHEI !!!')
    print('eu escolhi tesoura', emoji.emojize(':victory_hand:'))
elif e == 2 and e == 2:
    print('EMPATOU !!!')
    print('eu também escolhi papel', emoji.emojize(':hand_with_fingers_splayed:'))
if e == 3 and c == 2:
    print('VOCÊ GANHOU !!!')
    print('eu escolhi papel', emoji.emojize(':hand_with_fingers_splayed:'))
elif e == 3 and c == 1:
    print('EU GANHEI !!!')
    print('eu escolhi pedra', emoji.emojize('\U0001f44a\U0001f3fb'))
elif e == 3 and c == 3:
    print('EMPATOU !!!')
    print('eu também escolhi tesoura', emoji.emojize(':victory_hand:'))
