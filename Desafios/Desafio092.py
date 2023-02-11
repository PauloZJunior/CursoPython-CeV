from datetime import date
inf = dict()
inf['nome'] = str(input('Nome: '))
inf['idade'] = int(input('Ano de nascimento: '))
inf['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if inf['ctps'] != 0:
    inf['contratação'] = int(input('Ano de contratação: '))
    inf['salário'] = float(input('Salário: R$'))
print('-=' * 50)
print(inf)
print(f'Seu nome é: {inf["nome"]}')
print(f'Sua idade é: {date.today().year - inf["idade"]} anos.')
print(f'Sua carteira de trabalho é: {inf["ctps"]}')
if inf['ctps'] != 0:
    print(f'Sua contratação foi em: {inf["contratação"]}')
    print(f'Seu salário é de: {inf["salário"]}')
    print(f'Sua aposentadoria será em: {inf["contratação"] + 35} e você terá: {(inf["contratação"] + 35) - inf["idade"]} anos.')
