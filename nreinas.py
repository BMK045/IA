
#ARMANDO DANIEL SAUCEDO ALEGRIA#
#COBOS VALDEZ JESUS RICARDO#


def entrada(matriz,fila,columna):
	M = len(matriz)
	for i in range(columna):
		if matriz[fila][i] == "2":
			return False
	for i in range(columna,M,1):
		if matriz[fila][i] == "2":
			return False
	for f,c in zip(range(fila,-1,-1), range(columna,-1,-1)):
		if matriz[f][c] == "2":
			return False
	for f,c in zip(range(fila, M, 1), range(columna,-1,-1)):
		if matriz[f][c] == "2":
			return False
	for f,c in zip(range(fila,-1,-1), range(columna,N,1)):
		if matriz[f][c] == "2":
			return False
	for f,c in zip(range(fila,M,1), range(columna,N,1)):
		if matriz[f][c] == "2":
			return False
	return True

def iterar(matriz,columna):
	X = len(matriz)
	if columna >=X:
		return True
	if colmOcupada(matriz,columna):
		if iterar(matriz,columna + 1)== True:
			return True
			
	for i in range(X):
		if entrada(matriz,i,columna):
			matriz[i][columna] = "2"
			if iterar(matriz, columna + 1) == True:
				return True
			
			matriz[i][columna] = 0
		matriz[i][columna] = 0
	return False
	
def colmOcupada (matriz,columna):
	X = len(matriz)
	for i in range(X):
		if matriz[i][columna]== "2":
			return True
	return False

def impMatriz(matriz):
	X = len(matriz)
	for i in range(X):
		for j in range(X):
			print(matriz[i][j],end = " ")
		print()

def reina(matriz):
	if iterar(matriz,0)== False:
		print("\n No hay Solución")
		return False
		
	print ("\n Solucion")
	impMatriz(matriz)
	return True

def Ceros(N):
	Lista = []
	for i in range(N):
		Lista.append(0)
	return Lista
	
N = int(input("Cual es el tamaño de la matriz"))
f = int(input("Fila en donde se encuentra la reina"))
c = int(input("Columna donde se encuentra la reyna"))

matriz = []
for i in range(N):
	matriz.append(Ceros(N))
matriz[f][c]="2"
reina(matriz)


