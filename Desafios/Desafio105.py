def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias notas).
    :param sit: (valor opcional) indica se deve ou não adicionar a situação.
    :return: retorna um dicionário com várias informações sobre a situação da turma.
    """
    val = dict()
    val['total'] = len(n)
    val['maior'] = max(n)
    val['menor'] = min(n)
    val['média'] = sum(n) / len(n)
    if sit:
        if val['média'] >= 7:
            val['situação'] = 'BOM'
        elif val['média'] >= 5:
            val['situação'] = 'RAZOÁVEL'
        else:
            val['situação'] = 'RUIM'
    return val


#programa principal
resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
