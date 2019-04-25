#Modos de usar um dicionario

#UTILIZANDO O METODO DICT
#O modo é composto de uma variavel na qual sera o dicionario.
#Chamamos o metodo dict() e passamos as chaves e seus respectivos valores dentro dos parenteses
#A chave do dicionario não leva aspas
familia = dict(mae = 'Kelly', pai = 'Silvio', irmao = 'Rafa', irma='Mirela')

###########################################################################################################
#CRIANDO O DICIONARIO ANTES
#Primeiro criamos o dicionario usando colchetes {}
#Passamos a chave do dicinario entre chaves[] e entre aspas '' pois é uma string
#Depois, fora das chaves atribuimos um valor àquela chave
linguagens = {}
linguagens['forte'] = 'Python'
linguagens['media'] = 'Java'
linguagens['media-forte'] = 'Node'

###########################################################################################################
#ATRIBUINDO DIVERSOS VALORES
#Esse modo é uma mistura dos dois
#Primeiro atribuimos o dicionario a uma variavel e abrimos colchetes
#Dentro dos colchetes passamos a chave entre aspas 
#E por meio dos dois pontos : atribuimos um valor aquela chave
#Lembrando sempre de colocar virgula depois de cada declaração.
carros = {
	'hb20': 'Preto',
	'corsa': 'Amarelo',
	'c5': 'Prata'
}

###########################################################################################################
#Em dicionarios podemos localizar facilmente um valor passando a chave dele da seuginte forma
print('\nSua mae e a: {}'.format(familia['mae']))
print('Seu pai e o: {}'.format(familia['pai']))
print('Seu irmao e o: {}'.format(familia['irmao']))
print('Sua irma e a: {}'.format(familia['irma']))

print('\nVoce e forte na linguagem: {}'.format(linguagens['forte']))
print('Voce e medio na linguagem: {}'.format(linguagens['media']))
print('Voce e medio-forte na linguagem: {}'.format(linguagens['media-forte']))

print('\nO hb20 e: {}'.format(carros['hb20']))
print('O corsa e: {}'.format(carros['corsa']))
print('O c5 e: {}'.format(carros['c5']))

##########################################################################################################
#Podemos ainda chamar alguns metodos como o keys() e o values()
#keys() mostra todas as chaves do dicionario desejado
#values() mostra todos os valores contidos no dicionario desejado

print('\nAs chaves do dicionario carros sao: {}'.format(carros.keys()))
print('Os valores do dicionario carros sao: {}'.format(carros.values()))

print('\nAs chaves do dicionario familia sao: {}'.format(familia.keys()))
print('Os valores do dicionario familia sao: {}'.format(familia.values()))

print('\nAs chaves do dicionario linguages sao: {}'.format(linguagens.keys()))
print('Os valores do dicionario linguagens sao: {}'.format(linguagens.values()))

##########################################################################################################
#ITERANDO DICIONARIOS
#Existem duas formas de iterar em um dicionario 
#A primeira delas consiste em um loop que para cada item no dicionario ele retorna a key
#Entao fazemos a iteracao do proprio dicionario passando o item recebido como chave do dicionario
#Entao para cada carro no dicionario carro ele retorna a key e o carro/value
#Para cada integrante da familia ele retorna a funcao/key e o integrante/value
#Para cada linguagem ele retorna o nivel/key e a linguagem/value

print('\n')

for carro in carros:
	print("{} - {}".format(carro, carros[carro]))

print('\n')

for integrante in familia:
	print('{} - {}'.format(integrante, familia[integrante]))

print('\n')

for nivel in linguagens:
	print('{} - {}'.format(nivel, linguagens[nivel]))

#Entretanto isso nao é muito recomendado pela comunidade
#O modo mais correto é iterando dois itens no dicionario.items() que é uma funcao do python
#Dessa forma, para cada item, ele retorna a key e o value e joga nas variaveis de iteração
print('\n')
for key, value in carros.items():
	print('{} - {}'.format(key, value))

print('\n')
for chave, valor in familia.items():
	print('{} - {}'.format(chave, valor))

print('\n')
for nivel, linguagem in linguagens.items():
	print('{} - {}'.format(nivel, linguagem))
	
