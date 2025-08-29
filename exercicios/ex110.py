#Adicione ao modulo moeda.py criado nos desafios anteriosres, uma funcao chamada resumo(), que mostra na tela algumas informacoes geradas pelas funcoes que ja temos no modulo criado ate aqui
from modulos_pacotes.moeda import moeda_resumo

preco = float(input('Digite o preço: R$ '))
moeda_resumo.resumo(preco, 80, 35)