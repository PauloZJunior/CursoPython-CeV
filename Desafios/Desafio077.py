p = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
     'programador', 'futuro')
for c in range(len(p)):
    print(f'Na palavra {p[c].upper():11} temos: ', end='')
    for d in range(len(p[c])):
        if p[c][d] in 'aeiou':
            print(f'{p[c][d]:<2}', end='')
    print(' ')
