## Abaixo se encontram as 4 quest�es do seu teste de L�gica de Programa��o.
## Implemente todas elas neste arquivo seguindo os padr�es da linguagem escolhida e utilizando os cabe�alhos das fun��es.
## As suas respostas ser�o corrigidas analisando a l�gica utilizada, a sua familiaridade com a linguagem e ser�o submetidas a casos de teste al�m dos exemplos presentes nesse arquivo.
## Vale lembrar que voc� tem at� 2 horas, a partir do recebimento do e-mail em hor�rio combinado anteriormente, para fazer o m�ximo de quest�es que conseguir.
## Por favor, confirme o recebimento deste teste antes de inici�-lo.
## Boa sorte!!


## Dist�ncia Vogal
# Escreva uma fun��o que recebe uma string e retorne uma outra string onde cada caracter � trocado pela sua dist�ncia at� a vogal mais pr�xima. Por exemplo, para a palavra "chama" deve ser retornado "21010", pois o 'c' est� a 2 caracteres da vogal mais pr�xima, o 'a', o 'h' est� a 1 s�, e assim por diante. Vale destacar que quando o caracter em si � um vogal, � retornado um 0 para ele.


## Exemplos Python:
# >>> distancia_vogal("aaaaa")
# >>> "00000"
# 
# >>> distancia_vogal("babbb")
# >>> "10123"
#
# >>> distancia_vogal("abcdabcd")
# >>> "01210123"
#
# >>> distancia_vogal("shopper")
# >>> "2101101"

def distancia_vogal(palavra):
	s = ''
	for i in palavra:
		da = abs(ord(i.upper()) - ord('A'))
		de = abs(ord(i.upper()) - ord('E'))
		di = abs(ord(i.upper()) - ord('I'))
		do = abs(ord(i.upper()) - ord('O'))
		du = abs(ord(i.upper()) - ord('U'))

		s = s + str(min(da, de, di, do, du))

	return s


## Ponte Quebrada
# Uma ponte quebrada pode ser representada por 1s e 0s, por exemplo [1, 1, 1, 1, 0, 1, 0, 1], onde os 0s continuos representam buracos.
# Voc� consegue cruzar uma ponte, caso ela tenha buracoes de no m�ximo 1 de largura, como no exemplo dado. Caso a ponte tenha buracos maiores, � necess�rio consertar tais buracos oara atravess�-la.

# A seguinte ponte � caminh�vel: [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1]
# J� essa outra n�o �: [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], pois tem um buraco de tamanho 2.
# Por�m, se voc� tiver uma t�bua de madeira de tamanho 1 ou 2, voc� pode consertar a ponte acima e assim conseguir cruz�-la.
# Com uma t�bua de tamanho 2 ela fica assim [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] e com uma de tamanho 1 assim [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1].
# Mais especificamente, um tamanho de t�bua n pode cobrir um buraco de tamanho n. Por�m, se voc� tiver 2 t�buas, n�o pode combin�-las para formar uma t�bua maior, apenas uma t�bua pode ser usada por buraco na ponte. Al�m disso, uma t�bua precisa sempre de ao menos um lado para se apoiar, ou seja, na ponte [1, 0, 0, 0, 1], se voc� tiver uma t�bua de tamanho 1, n�o tem como coloc�-la na terceira posi��o para cruzar a ponte. Nesse caso � False.

# Assim, escreva uma fun��o que recebe um vetor representando uma ponte quebrada e lista de tamanhos de t�buas dispon�vels e retorne True se a ponte pode ser consertada para que se possa caminhar, e False caso contr�rio.


## Exemplos Python:
# >>> conserto_ponte([1, 0, 0, 0, 0, 0, 0, 1], [5, 1, 2]) 
# >>> True
#
# >>> conserto_ponte([1, 0, 0, 0, 0, 0, 0, 1], [4, 1, 2, 3, 4]) 
# >>> False
# 
# >>> conserto_ponte([1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 2]) 
# >>> True
#
# >>> conserto_ponte([1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 1]) 
# >>> False


def conserto_ponte(ponte, tabuas):
	buracos  = []
	tamanho_buraco = 0
	for i in ponte:
		if i == 0:
			tamanho_buraco+=1
		elif i == 1 and tamanho_buraco!=0:
			buracos.append(tamanho_buraco)
			tamanho_buraco = 0	

	count = 0
	result = []

	if len(buracos) > 1:
		for t in tabuas:
			for b in buracos:
				dif = abs(t-b)
				if dif <= 1:
					result.append(True)
				
		if len(result) > len(buracos):
			return True
		else:
			return False				

	elif len(buracos) == 1:
		for i in tabuas:
			dif = abs(i-buracos[0])
			if dif <= 1:
				return True 
			else:
				return False


## Sinuca
# Sabe-se que em um jogo de sinuca, quanto mais pr�ximas as bolas est�o da bola branca, mais f�cil � acert�-las. Assim, dada a quantidade de bolas em uma mesa, a posi��o (x,y) de cada uma delas, e a posi��o (x,y) da bola branca, escreva uma fun��o que retorne qual a bola mais pr�xima. Havendo empate, deve ser retornada aquela de menor n�mero. 


## Exemplos Python:
# >>> sinuca(1, [(900, 1800)], (30, 60))
# >>> 1
#
# >>> sinuca(2, [(710, 2100),(710, 1000)], (710, 30))
# >>> 2
# 
# >>> sinuca(3, [(710, 2100),(510, 1000),(910, 1000)], (710, 30))
# >>> 2

#python 3.6.8 a minha maquina, tive cm usar essa lib pra n precisar implementar
#pyhon 3.8 + tem o math.dist
from scipy.spatial.distance import euclidean

def sinuca(n, posicao_bolas, posicao_branca):
	distances = [euclidean(p, posicao_branca) for p in posicao_bolas]
	m = min(distances)
	id = distances.index(m)
	return id+1



# sinuca(3, [(710, 2100),(510, 1000),(910, 1000)], (710, 30))

## D�gito verificador
# O d�gito verificador � um mecanismo de autentica��o utilizado para verificar a
# validade e a autenticidade de um valor num�rico, evitando dessa forma fraudes ou erros
# de transmiss�o ou digita��o. Consiste em um ou mais d�gitos acrescentados ao valor
# original e calculados a partir deste atrav�s de um determinado algoritmo. N�meros de
# documentos de identifica��o, de matr�cula, cart�es de cr�dito e quaisquer outros
# c�digos num�ricos, que necessitem de maior seguran�a, utilizam d�gitos verificadores
# (Wikipedia).

# Uma das rotinas mais tradicionais para c�lculo do d�gito verificador � denominada
# M�dulo 11, que funciona da seguinte forma: cada d�gito do n�mero, come�ando da direita
# para a esquerda (menos significativo para o mais significativo) � multiplicado, na ordem,
# por 2, depois 3, depois 4 e assim sucessivamente, at� o limite de multiplica��o escolhido.
# Ent�o novamente multiplica-se o n�mero por 2, 3, etc. O resultado de cada uma dessas
# multiplica��es � somado e depois multiplicado por 10 e por fim dividido pelo m�dulo escolhido,
# o digito ser� o resto dessa divis�o inteira.
# exemplo para numero 2615338 (digito verificador = 8) com limite de multiplica��o 5 em m�dulo 11:

#   2      6       1     5       3     3    -    8
#  x3     x2      x5    x4      x3    x2
#  6     12       5    20       9     6
#  6  +  12 +  5 +  20 +   9  +  6    =    58 x 10 = 580) / 11 = 52, resto 8 => DV = 8

# Escreva um programa que receba um n�mero inteiro, juntamente com um digito verificador.
# Calcule o d�gito verificador do n�mero usando a t�cnica descrita acima, considerando que o
# limite de multiplica��o (ap�s a multiplica��o pelo limite, a multiplica��o retorna a 2) e
# o m�dulo s�o passados como parametro.
# O algoritmo deve retornar 1, se o n�mero � v�lido ou 0 caso n�o seja


## Exemplos Python:
# >>> digito_verificador(2615338, 5, 11)
# >>> 1
#
# >>> digito_verificador(43245112, 7, 11)
# >>> 1
# 
# >>> digito_verificador(554805, 6, 7)
# >>> 1


def digito_verificador(numero, limMultiplicacao, modulo):
	st = str(numero)
	arr = st[0:len(st)-1]
	rev = arr[::-1]
	dv = int(st[-1])
	s = 0
	m = 2
	
	for i in rev:
		s += m*int(i)
		if m == limMultiplicacao:
			m = 2
		else:
			m+=1


	result = (s*10)%11
	print(result)
	if result == dv:
		return 1
	else:
		return 0
