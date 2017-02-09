from Tkinter import *
import ttk as ttk
import tkMessageBox
from collections import deque

###Globales####
begin = 1,1
end = 1,1
laberinto = {}
busqueda = []








matriz = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0],
          [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
          [0,1,1,0,0,1,0,0,1,0,0,0,0,0,1,0],
          [0,1,0,0,0,1,0,0,1,0,1,1,1,1,1,0],
          [0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0],
          [0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
#######################################Ponderacion#############################################
def ponderar(cam,dest):
    distancia = 0
    inix = cam[0]
    iniy = cam[1]
    desx = dest[0]
    desy = dest[1]
    if inix < desx:
        x = desx - inix
    else:
        x = inix - desx
    if iniy < desy:
        y = desy - iniy
    else:
        y = iniy - desy
    tmp = x ** 2 + y ** 2
    distancia = tmp ** .5
    return distancia
###############################################Busquedas################################
def limitada(deep):
    origen = busqueda[0]
    destino = busqueda[1]
    limite = int(deep)
    howdeep = {origen: 0}
    abiertos = deque()
    cerrados = set()
    terminal = {origen: [origen]}
    abiertos.append(origen)
    while abiertos:
        actual = abiertos.popleft()
        if actual == destino:
            path = terminal[actual]
            grafica(path,'aqua')
            break
        cerrados.add(actual)
        if howdeep[actual] < limite:
            for ruta in grafo[actual]:
                if not abiertos.count(ruta):
                    abiertos.append(ruta)
                    ####genera profundidad
                    howdeep[ruta] = howdeep[actual] + 1
                    ####genera ruta
                    temporal = []
                    temporal = temporal + terminal[actual]
                    temporal.append(ruta)
                    terminal[ruta] = temporal
        else:
            tkMessageBox.showinfo("Thats what she said", "Busca mas profundo")
            break
def iteracion():
    origen = busqueda[0]
    destino = busqueda[1]
    howdeep = {origen:0}
    abiertos = deque()
    cerrados = set()
    terminal = {origen: [origen]}
    abiertos.append(origen)
    while abiertos:
        actual = abiertos.popleft()
        if actual == destino:
            path = terminal[actual]
            tkMessageBox.showinfo("profundidad actual", howdeep[actual])
            grafica(path,'green')
            break
        cerrados.add(actual)
        for ruta in grafo[actual]:
            if not abiertos.count(ruta):
                abiertos.append(ruta)
                ####genera profundidad
                howdeep[ruta] = howdeep[actual] + 1
                ####genera r uta
                temporal = []
                temporal = temporal + terminal[actual]
                temporal.append(ruta)
                terminal[ruta] = temporal
def anchura():
    origen = busqueda[0]
    destino = busqueda[1]
    abiertos = deque()
    cerrados = set()
    road = {origen :[origen]}
    abiertos.append(origen)
    while abiertos:
        actual = abiertos.pop()  #Asignacion del actual
        if actual == destino:
            path = road[destino]
            return grafica(path,'blue')

        cerrados.add(actual)
        for ruta in grafo[actual]:
            if ruta not in cerrados and not abiertos.count(ruta) == 1 :
                abiertos.append(ruta)
                temporal = []
                temporal =temporal + road[actual]
                temporal.append(ruta)
                road[ruta] = temporal
    tkMessageBox.showinfo("No encontrado")
def profundidad():
    origen = busqueda[0]
    destino = busqueda[1]
    print origen,destino
    abiertos = deque()
    cerrados = set()
    terminal = {origen:[origen]}
    abiertos.append(origen)
    while abiertos:
        actual = abiertos.popleft()
        if actual == destino:
            path = terminal[destino]
            grafica(path,'red')
        cerrados.add(actual)
        #print 'actual ',actual
        for cam in grafo[actual]:
            if cam not in cerrados and not abiertos.count(cam) == 1:
                abiertos.append(cam)
                temporal = []
                temporal = temporal + terminal[actual]
                temporal.append(cam)
                #print temporal
                #print cam
                terminal[cam] = temporal

def climbing():
    origen = busqueda[0]
    destino = busqueda[1]
    distMayor = ponderar(origen,destino)
    howdeep = {origen: 0}
    abiertos = deque()
    cerrados = set()
    terminal = {origen: [origen]}
    abiertos.append(origen)
    actual = abiertos
    while abiertos:
        actual = abiertos.popleft()
        if actual == destino:
            path = terminal[destino]
            grafica(path, 'pink')
            break
        cerrados.add(actual)
        for rut in grafo[actual]:
            howdeep[rut] = howdeep[actual] + 1
        for cam in grafo[actual]:
            if cam not in cerrados and not abiertos.count(cam) == 1:
                if howdeep[cam] <= distMayor +1 :
                    abiertos.append(cam)
                    temporal = []
                    temporal = temporal + terminal[actual]
                    temporal.append(cam)
                    terminal[cam] = temporal

    for cam,val in terminal.iteritems():
        grafica(val,'pink')

    tkMessageBox.showinfo("Maximo local :(")


def estrella():
    distancias = {}
    origen = busqueda[0]
    destino = busqueda[1]
    distancias[origen] = ponderar(origen,destino)
    #print origen, destino
    abiertos = deque()
    cerrados = set()
    terminal = {origen: [origen]}
    abiertos.append(origen)
    while abiertos:
        distanciasTMP = {}
        actual = abiertos.popleft()
        if actual == destino:
            path = terminal[destino]
            grafica(path, 'orange')
        cerrados.add(actual)
        # print 'actual ',actual
        menor = 0
        for rut in grafo[actual]:
            distanciasTMP[rut] = ponderar(rut,destino)
            distancias[rut] = ponderar(rut,destino)
        sorted(distanciasTMP.values())
        print distanciasTMP
        for cam,val in distanciasTMP.iteritems():
            if cam not in cerrados and not abiertos.count(cam) == 1:
                #if val <= distancias[actual]:
                abiertos.append(cam)
                temporal = []
                temporal = temporal + terminal[actual]
                temporal.append(cam)
                # print temporal
                # print cam
                terminal[cam] = temporal
    #tkMessageBox.showinfo("Maximo local :(")
#########################################OnClick########################################
def seleccion(nombre):
    begin = nombre
    laberinto[nombre].config(bg="green")
    busqueda.append(nombre)
    print busqueda

def reset():
    del busqueda[:]
    x = 0
    y = 0
    z = 0
    for i in matriz:
        for j in i:
            if j == 0:
                c = 'black'
            else:
                c = 'white'
            name = x, y
            laberinto[name].config(bg=c)
            y = y + 1
            z = z + 1
        x = x + 1
        y = 0

#################################Matriz a lista########################################
root = Tk()
root.wm_title("Crucigrama")
# tamano de la ventana
root.geometry("800x300")


grafo = {}
k=0
for i in matriz:
    h=0
    for j in i:
        if j == 1:
            destinos = []
            if matriz[k-1][h] == 1:
                opc = k-1,h
                destinos.append(opc)
            if matriz[k][h-1] == 1:
                opc = k,h-1
                destinos.append(opc)
            if matriz[k+1][h] == 1:
                opc = k+1,h
                destinos.append(opc)
            if matriz[k][h+1] == 1:
                opc = k,h+1
                destinos.append(opc)
            name = k,h
            grafo[name] = destinos
        h=h+1
    k=k+1
#print grafo

#############################################Dibujar camino###############################################
def grafica(rutas,color):
    for ruta in rutas:
        laberinto[ruta].config(bg=color)

########################Graficar1#################################################################
x = 0
y = 0
z=0
for i in matriz:
    for j in i:
        if j == 0:
            c = 'black'
        else:
            c = 'white'
        name = x,y
        laberinto[name] = Button(root, height=1, width=1, bg=c,command = lambda nombre=name: seleccion(nombre))
        laberinto[name].grid(row=x, column=y)
        y = y + 1
        z=z+1
    x = x + 1
    y = 0
##########################Botones de busqueda############################################################
num = ttk.Combobox(root,width =2,values = [1,2,3,4,5,6,7,8,9,10])
num.set(1)
num.place(x=590,y=75)

# Crea instancia del boton
limi = Button(root,text = "Profundidad limitada",command = lambda : limitada(num.get()))
iter = Button(root,text = "Profundidad iterativa",command = iteracion)
hill = Button(root,text = "Hill climbing",command = climbing)
A = Button(root,text = "A*",command = estrella)
profunda = Button(root, text="Profundidad",command= profundidad)
anchu = Button(root, text="Anchura",command = anchura)
res = Button(root,text='Reset',command = reset)

# Coloca el boton
limi.place(x = 450,y = 75)
iter.place(x = 650,y = 75)
hill.place(x=680,y=125)
profunda.place(x=590, y=125)
anchu.place(x=500, y=125)
res.place(x=600,y=200)
A.place(x = 680,y = 200)

Tk.mainloop(root)