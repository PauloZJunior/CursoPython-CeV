from datetime import date
a = int(input('Digite o ano em que você nasceu: '))
d = date.today().year
i = d - a
if i < 18:
    print(f'Ainda faltam {18 - i} anos para você se alistar.')
elif i == 18:
    print('Você precisa se alistar esse ano.')
else:
    print(f'Já passou {d - (a + 18)} anos do prazo de alistamento.')
