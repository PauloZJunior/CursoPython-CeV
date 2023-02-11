import requests

try:
    s = requests.get('http://www.pudim.com.br')
except Exception as erro:
    print('\033[1;31mSite pudim não está acessível no momento! Tente novamente mais tarde!\033[m')
else:
    print('\033[1;32mSite pudim foi acessado com sucesso!\033[m')
