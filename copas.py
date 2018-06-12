selecoes_participacoes = {'Russia': [1958,1962,1966,1970,1982,1986,1990,1994,2002,2014],
						  'ArabiaSaudita': [1994,1998,2002,2006],
						  'Egito': [1934,1990],
						  'Uruguai': [1930,1950,1954,1962,1966,1970,1974,1986,1990,2002,2010,2014],
						  'Portugal': [1966,1986,2002,2006,2010,2014],
						  'Espanha': [1934,1950,1962,1966,1978,1982,1986,1990,1994,1998,2002,2006,2010,2014],
						  'Marrocos': [1970,1986,1994,1998],
						  'Ira': [1978,1998,2006,2014],
						  'Franca': [1930,1934,1938,1954,1958,1966,1978,1982,1986,1998,2002,2006,2010,2014],
						  'Australia': [1974,2006,2010,2014],
						  'Peru': [1930,1970,1978,1982],
						  'Dinamarca': [1986,1998,2002,2010],
						  'Argentina': [1930,1934,1958,1962,1966,1974,1978,1982,1986,1990,1994,1998,2002,2006,2010,2014],
						  'Islandia': [],
						  'Croacia': [1998,2002,2006,2014],
						  'Nigeria': [1994,1998,2002,2010,2014],
						  'Brasil': [1930,1934,1938,1950,1954,1958,1962,1966,1970,1974,1978,1982,1986,1990,1994,1998,2002,2006,2010,2014],
						  'Suica': [1934,1938,1950,1954,1962,1966,1994,2006,2010,2014],
						  'CostaRica': [1990,2002,2006,2014],
						  'Servia': [1998,2006,2010],
						  'Alemanha': [1934,1938,1954,1958,1962,1966,1970,1974,1978,1982,1986,1990,1994,1998,2002,2006,2010,2014],
						  'Mexico': [1930,1950,1954,1958,1962,1966,1970,1978,1986,1994,1998,2002,2006,2010,2014],
						  'Suecia': [1934,1938,1950,1958,1970,1974,1978,1990,1994,2002,2006],
						  'CoreiaDoSul': [1954,1986,1990,1994,1998,2002,2006,2010,2014],
						  'Belgica': [1930,1934,1938,1954,1970,1982,1986,1990,1994,1998,2002,2014],
						  'Panama': [],
						  'Tunisia': [1978,1998,2002,2006],
						  'Inglaterra': [1950,1954,1958,1962,1966,1970,1982,1986,1990,1998,2002,2006,2010,2014],
						  'Polonia': [1938,1974,1978,1982,1986,2002,2006],
						  'Senegal': [2002],
						  'Colombia': [1962,1990,1994,1998,2014],
						  'Japao': [1998,2002,2006,2010,2014]}

selecoes = list(selecoes_participacoes)
print(type(selecoes))
anos = selecoes_participacoes['Brasil']

file = open('copas.csv', 'w')
file.write('selecao,ano,vit-amistosos,der-amistosos,emp-amistosos,sdg-amistosos,vit-eliminatorias,der-eliminatorias,emp-eliminatorias,sdg-copa,vit-copa,der-copa,emp-copa,sdg-copa,classificacao\n')

exemplos = 0
for ano in anos:
	count = 0
	for selecao in selecoes:
		for i in range(len(selecoes_participacoes[selecao])):
			if (selecoes_participacoes[selecao][i] == ano): 
				count+=1
				file.write(selecao + ',' + str(ano) + ',,,,,,,,,,,,,\n')
	print(ano, ': ', count, 'seleções')
	exemplos+=count

print("Número de exemplos no dataset: ", exemplos)




file.close()