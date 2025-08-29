#Dentro do pacote modulos_pacotes que criamos no desafio 111, teremos um modulo chamado dado. Crie uma funcao chamada leiaDinheiro() que seja capaz de funcionar como a funcao input() mas com uma validacao de dados para aceitar apenas valores que sejam monetarios
from modulos_pacotes.dado import dado
from modulos_pacotes.moeda import moeda_resumo

num = dado.leiaDinheiro('Digite o preço: R$ ')
moeda_resumo.resumo(num, 80, 35)