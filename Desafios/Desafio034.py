s = float(input('Qual o salário do funcionário? R$'))
if s > 1250:
    print(f'O novo salário do funcionário com aumento de 10% será de :R${s+(s*0.1):.2f}.')
else:
    print(f'O novo salário do funcionário com aumento de 15% será de :R${s+(s*0.15):.2f}')
