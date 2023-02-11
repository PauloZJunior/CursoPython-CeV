def area(a, b):
    c = a * b
    print(f'A área de um terreno de {a}m x {b}m é de {c}m²')


print('Controle de Terrenos')
print('-=' * 15)
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
