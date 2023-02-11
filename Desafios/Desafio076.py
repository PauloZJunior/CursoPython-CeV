f = 'LISTAGEM DE PREÇOS'
l = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila',
         120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-'*50)
print(f'{f:^50}')
print('-'*50)
for c in range(len(l)):
    if c % 2 == 0:
        print(f'{l[c]:.<40}R${l[c + 1]:>7.2f}')
print('-'*50)
