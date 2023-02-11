import moeda

n = float(input('Digite o preço: R$'))
print(f'O dobro de {n} é: ', moeda.dobro(n))
print(f'A metade de {n} é: ', moeda.metade(n))
print(f'{n} mais 10% é: ', moeda.aumentar(n, 10))
print(f'{n} menos 13% é: ', moeda.diminuir(n, 13))
