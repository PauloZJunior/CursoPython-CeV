v = int(input('Qual a velocidade do carro? '))
if v > 80:
    print(f'Você ultrapassou o limite de 80km/h. Sua multa é: R${(v - 80)*7:.2f}')
else:
    print('Você está dentro do limite de velocidade, parabéns!')
