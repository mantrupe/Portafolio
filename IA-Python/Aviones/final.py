from Tkinter import *
import ttk as ttk
import tkMessageBox
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import json
from collections import deque
from math import radians, cos, sin, asin, sqrt


def ponderar(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

####################################################################################################################
#Decodificacion de Json
info = [] #Lista que recibe el json
with open("grafojson.json") as json_data :
    for line in json_data:
        info.append(json.loads(line))
grafo = {}
rutas = []
opciones = []
ciudades = {}
destinos = []
destino = str
for airport in info[0]['airports']:
    destinos = []
    city = airport['cityCode']
    coordenadas = airport['coordinates']
    coordenadas ={str(k):int(v) for k,v in coordenadas.items()}#transforma key value de diccionario en string
    ciudades[str(city)] = coordenadas
    for ruta in airport['routes']:
        if ruta[0] == 'c' and  ruta[3] == 'y':
            x = len(ruta)
            destino = ruta[5:x]
            destinos.append(str(destino))
    nodo = {city: destinos}
    opciones.append(str(city))
    grafo[city] = destinos

#########################################################################################################
def grafica(caminos):
    lat = []
    lon = []
    for rut in caminos:
        latitud = ciudades[rut]['latitude']
        longitud = ciudades[rut]['longitude']
        lat.append(latitud)
        lon.append(longitud)
    my_map = Basemap(projection='mill', llcrnrlat=30, urcrnrlat=70, llcrnrlon=-30, urcrnrlon=60,
                     resolution='c', area_thresh=1000.0)
    my_map.drawcountries()
    my_map.bluemarble()
    x, y = my_map(lon, lat)
    my_map.plot(x, y, "ro" )
    my_map.plot(x, y,linewidth=1, color='aqua',)


    plt.show()
############################################################################################################
def heuristica(origen,destino):
    mejor = []
    abiertos = deque()
    cerrados = set()
    terminal = {origen: [origen]}
    abiertos.append(origen)
    while abiertos:
        actual = abiertos.popleft()
        if actual == destino:
            path = terminal[destino]
            grafica(path)
            break
        cerrados.add(actual)
        for ruta in grafo[actual]:
            if not abiertos.count(ruta):
                abiertos.append(mejor)
                temporal = []
                temporal = temporal + terminal[actual]
                temporal.append(ruta)
                terminal[ruta] = temporal

    tkMessageBox.showinfo("No encontrado")


def anchura(origen,destino):
    abiertos = deque()
    cerrados = set()
    road = {origen :[origen]}
    abiertos.append(origen)
    while abiertos:
        actual = abiertos.pop()  #Asignacion del actual
        if actual == destino:
            path = road[destino]
            grafica(path)
            break
        cerrados.add(actual)
        for ruta in grafo[actual]:
            if ruta not in cerrados and not abiertos.count(ruta) == 1 :
                abiertos.append(ruta)
                temporal = []
                temporal =temporal + road[actual]
                temporal.append(ruta)
                road[ruta] = temporal
    tkMessageBox.showinfo("No encontrado")

def profundidad(origen,destino):
    abiertos = deque()
    cerrados = set()
    terminal = {origen:[origen]}
    abiertos.append(origen)
    while abiertos:
        actual = abiertos.popleft()
        if actual == destino:
            path = terminal[destino]
            grafica(path)
            break
        cerrados.add(actual)
        for ruta in grafo[actual]:
            if not abiertos.count(ruta):
                abiertos.append(ruta)
                temporal = []
                temporal = temporal + terminal[actual]
                temporal.append(ruta)
                terminal[ruta] = temporal
    tkMessageBox.showinfo("No encontrado")

def iteracion(origen,destino):
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
            grafica(path)
            break
        cerrados.add(actual)
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


def limitada(origen, destino, deep):
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
            grafica(path)
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

def climbing(origen,destino):
    distMayor = ponderar(ciudades[origen]['longitude'],ciudades[origen]['latitude'],ciudades[destino]['longitude'],ciudades[destino]['latitude'])
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
            grafica(path)
            break
        cerrados.add(actual)
        for rut in grafo[actual]:
            howdeep[rut] = howdeep[actual] + ponderar(ciudades[actual]['longitude'],ciudades[actual]['latitude'],ciudades[rut]['longitude'],ciudades[rut]['latitude']
)
        for cam in grafo[actual]:
            if cam not in cerrados and not abiertos.count(cam) == 1:
                if howdeep[cam] <= distMayor:
                    abiertos.append(cam)
                    temporal = []
                    temporal = temporal + terminal[actual]
                    temporal.append(cam)
                    terminal[cam] = temporal
    tkMessageBox.showinfo("Maximo local :(")
    path = terminal[actual]
    grafica(path)


def estrella(origen,destino):
    distancias = {}
    distancias[origen] = ponderar(ciudades[origen]['longitude'],ciudades[origen]['latitude'],ciudades[destino]['longitude'],ciudades[destino]['latitude'])
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
            grafica(path)
        cerrados.add(actual)
        for rut in grafo[actual]:
            distanciasTMP[rut] = ponderar(ciudades[rut]['longitude'],ciudades[rut]['latitude'],ciudades[destino]['longitude'],ciudades[destino]['latitude'])
            distancias[rut] = ponderar(ciudades[rut]['longitude'],ciudades[rut]['latitude'],ciudades[destino]['longitude'],ciudades[destino]['latitude'])
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

############################################################################################################
root = Tk()
root.wm_title("Aviones")
# tamano de la ventana
root.geometry("800x175")

def client_exit():
    root.quit()
    root.destroy()



# label
o = Label(root, text="Origen")
d = Label(root, text="Destino")

#Coloca labels
o.place(x=100,y=50)
d.place(x=350,y=50)

# Spinbox
ori = ttk.Combobox(root, values=opciones)
ori.set("PARMA")
ori.place(x=50, y=75)

dest = ttk.Combobox(root, values=opciones)
dest.set("PARMA")
dest.place(x=300, y=75)

num = ttk.Combobox(root,width =2,values = [1,2,3,4,5,6,7,8,9,10])
num.set(1)
num.place(x=590,y=25)

# Crea instancia del boton
quitButton = Button(root, text="Cerrar", command=client_exit)
limi = Button(root,text = "Profundidad limitada",command = lambda : limitada(ori.get(),dest.get(),num.get()))
iter = Button(root,text = "Profundidad iterativa",command = lambda :iteracion(ori.get(),dest.get() ))
profunda = Button(root, text="Profundidad",command = lambda : anchura(ori.get(),dest.get() ) )
anchu = Button(root, text="Anchura",command = lambda : profundidad(ori.get(),dest.get() ) )
hill = Button(root,text ="Hill climbing",command = lambda:climbing(ori.get(),dest.get() ) )
A =Button(root,text = "A*" , command = lambda:estrella(ori.get(),dest.get() ) )

# Coloca el boton
quitButton.place(x=700, y=75)
limi.place(x = 450,y = 25)
iter.place(x = 650,y = 25)
profunda.place(x=590, y=75)
anchu.place(x=500, y=75)
hill.place(x= 500,y = 125)
A.place(x=650,y=125)


Tk.mainloop(root)