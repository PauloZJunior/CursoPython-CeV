from datetime import date
a = int(input('Informe o ano de nascimento: '))
i = date.today().year - a
if i <= 9:
    print('Sua categoria é: MIRIM')
elif i <= 14:
    print('Sua categoria é: INFANTIL')
elif i <= 19:
    print('Sua categoria é: JÚNIOR')
elif i <= 25:
    print('Sua categoria é: SÊNIOR')
elif i > 25:
    print('Sua categoria é: MASTER')
