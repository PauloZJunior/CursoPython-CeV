expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')


'''(JEITO ERRADO)
n = list()
n = input('Digite a expressão: ')
pa = 0
pf = 0
for c in range(len(n)):
    if n[c] == '(':
        pa += 1
    if n[c] == ')':
        pf += 1
if pa == pf:
    print('Sua expressão está CORRETA!')
else:
    print('Sua expressão está ERRADA!')'''