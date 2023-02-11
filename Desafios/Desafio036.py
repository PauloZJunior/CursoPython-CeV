v = float(input('Qual o valor da casa que você deseja comprar? R$'))
s = float(input('Qual o seu salário? R$'))
a = int(input('Em quantos anos você quer parcelar a casa? '))
p = (v / a) / 12
if p > (30/100) * s:
    print(f'A prestação mensal de R${p:.2f} excede 30% do seu salário, portanto seu empréstimo foi \033[31mNEGADO\033[m.')
else:
    print(f'Seu empréstimo foi \033[32mAPROVADO!\033[m A pestação mensal será de R${p:.2f} mensais.')
