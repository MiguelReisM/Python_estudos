#Modifique as funcoes que foram criadas no desafio 107 para que elas aceitem um parametro a mais, informando se o valor vai ser formatado pela funcao moeda(), desevolvida no desafio 108
from modulos_pacotes.moeda import moeda_formt_show

preco = float(input('Digite o preço: R$ '))
print(f"A metade de {moeda_formt_show.moeda(preco)} é {moeda_formt_show.metade(preco, formatar=False)}")
print(f"O dobro de {moeda_formt_show.moeda(preco)} é {moeda_formt_show.dobro(preco, formatar=False)}")
print(f"Com 10% de aumento: {moeda_formt_show.aumentar(preco, 10, formatar=True)}")
print(f"Com 13% de desconto: {moeda_formt_show.diminuir(preco, 13, formatar=True)}")