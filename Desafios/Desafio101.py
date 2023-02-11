def voto(nasc):
    from datetime import date
    h = date.today().year
    nasc = h - a
    if nasc < 16:
        return f'Com {nasc} anos: NÃO VOTA.'
    elif 16 <= nasc < 18 or nasc >= 65:
        return f'Com {nasc} anos: VOTO OPCIONAL.'
    else:
        return f'Com {nasc} anos: VOTO OBRIGATÓRIO.'


#programa principal
a = int(input('Digite o ano de nascimento: '))
print(voto(a))

