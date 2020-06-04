#ARMANDO DANIEL SAUCEDO ALEGRIA#
#COBOS VALDEZ JESUS RICARDO#


import json
import random
from operator import itemgetter

with open('subidadelacolina.json') as file:
	data = json.load(file)

ruta=[]
camino=[]
otro = []
def subidadelacolina(inicial,objetivo,ant):
    ruta.append(inicial)
    print("Inicial "+inicial)
    print("Anterior "+ant)
    if otro:
        del otro[:]
        del camino[:]
    if objetivo == inicial:
        print("encontrado")
        return inicial
    if ant == "":
        ant = inicial
    for d in data:
        if d[0] == inicial:
            if ant != "":
                if d[1] != ant:
                    camino.append(d)
    print(min(camino, key=itemgetter(2))[:])
    print (camino)
    chi = (min(camino, key=itemgetter(2))[2])
   
    for c in camino:
        if c[2] == chi:
            print("entra")
            otro.append(c)
    print("nnxt valores defintivos")
    print(otro)
    cont = 0
    for n in otro:
        cont = cont +1
        if cont > 1:
            r = random.random()
            print("n")
            print(n)
            if r < 0.5:
                otro.pop()
            else: 
                otro.pop(0)
        else:
            print(otro)
    if otro:
        for n in otro:
            print("nodo")
            print(n[1])
            return subidadelacolina(n[1],objetivo,inicial)

                
arch=subidadelacolina("Z","I","")
if arch:
    print("nodo")
    print(arch)
    print("ruta")
    print(ruta)
