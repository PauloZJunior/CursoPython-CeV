a = float(input('Informe a sua altura: '))
p = float(input('Informe seu peso: '))
imc = p / a ** 2
print(f'O seu IMC é: {imc:.2f}.')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está com o peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')
