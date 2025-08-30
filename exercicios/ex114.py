#Crie um codigo em Python que teste se o site Pudim esta acessivel pelo computador usado (https://www.pudim.com.br/)
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
    print('Foi possível acessar o site do Pudim!')
except:
    print('\033[31mErro! O site do Pudim não foi possível de ser acessado.\033[m')

