p = float(input('Qual o preço do produto? R$'))
print('='*50)
print('Digite o número referente a forma de pagamento.')
print('='*50)
print('1- À vista no dinheiro/cheque.\n2- À vista no cartão.\n3- Até 2x no cartão.\n4- 3x ou mais no cartão.')
print('='*50)
fp = int(input('Digite aqui o número: '))
if fp == 1:
    print(f'\nO valor do produto à vista no dinheiro ou cheque com desconto de 10% fica: R${p - (0.1*p):.2f}')
elif fp == 2:
    print(f'O valor do produto à vista no cartão com desconto de 5% fica: R${p - (0.05*p):.2f}')
elif fp == 3:
    print(f'O valor do produto em até 2x no cartão é: R${p}')
elif fp == 4:
    print(f'O valor do produto em 3x ou mais com juros de 20% fica: R${p + (0.2*p):.2f}')
else:
    print('Você digitou um número inválido, tente novamente mais tarde.')
