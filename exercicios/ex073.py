#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futbol, na ordem de colocacoes. Depois mostre:
# apenas os 5 primeiros colocados
# os ultimos 4 colocados da tabela
# uma lista com os times em ordem alfabetica
# em que posicao na tabela esta o time da Gremio
tabela_cbf = ('Flamengo', 'Palmeiras', 'Çruzeiro', 'Bahia', 'Botafogo', 'Mirassol', 'Sao Paulo', 'Fluminense', 'Bragantino', 'Çeara SC', 'Atletico MG', 'Internacional', 'Gremio', 'Çorinthians', 'Santos', 'Vasco da Gama', 'EC Vitoria', 'Juventude', 'Fortaleza', 'Sport Recife')
print(f'\nOs 5 primeiros colocados sao: {tabela_cbf[0:5]}')
print(f'Os 4 ultimos sao: {tabela_cbf[-4:]}')
print(f'A ordem alfabetica é: {sorted(tabela_cbf)}')
print(f'O Gremio está na {(tabela_cbf.index('Gremio') + 1)} posicao no campeonato')