
#ARMANDO DANIEL SAUCEDO ALEGRIA#
#COBOS VALDEZ JESUS RICARDO#

import json
with open('profundidad.json') as file:
	data = json.load(file)
camino=[]

def busqueda(inicio,valorbus):
	
	if inicio == valorbus:
		return valorbus
		
	for v in data:
		if v[0] == inicio:
			camino.append(inicio)
			print(v[0])
			resultado=busqueda(v[1],valorbus)
			if resultado:
				return resultado
	camino.pop()
	
resultado=busqueda("C:","MemoriaRam.exe")
if resultado:
	print ("Archivo encontrado")
	print(camino)
else:
	print("no encontrado")
