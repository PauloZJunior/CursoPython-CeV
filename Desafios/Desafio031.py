km = int(input('Qual a distância da viagem? '))
if km > 200:
    print(f'O custo para uma viagem de {km}km é de R${km * 0.45:.2f}.')
else:
    print(f'O custo para uma viagem de {km}km é de R${km * 0.50:.2f}.')
