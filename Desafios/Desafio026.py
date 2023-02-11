f = str(input('Digite uma frase: ')).lower().strip()
print('A sua frase tem ', f.count('a'), ' letras A.')
print('A primeira letra A aparece na posição: ', f.find('a')+1)
print('A última letra A aparece na posição: ', f.rfind('a')+1)
