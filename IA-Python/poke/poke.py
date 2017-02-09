import sys
import os
import json

class Arbol:
#*******Nodo
    def __init__(self,dato = None,si = None,no = None):
        self.dato = dato
        self.si = si
        self.no = no
    def __str__(self):
        return str(self.dato)
#*************Funciones
def loadTree(raiz,Array):
    raiz.dato =Array['dato']
    if Array['si'] != None:
        raiz.left = Arbol()
        loadTree(raiz.left, array["no"])
    if array["no"] != None:
        node.right = Node()
        loadTree(node.right,array["no"])
def si(preg):
    resp = input(preg).lower
    if resp == 'si':
        return (True)
    else:
        return (False)
def main():
    raiz = Arbol()
    file = open("pokemon.txt" , "r")
    file.seek(0)
    eof = file.read(1)
    if eof:
        file.seek(0)
        jsonRead = file.read()
        jsonArray = json.loads(jsonRead)
        loadTree(raiz,jsonArray)
        file.close()
    else:
        raiz = Arbol("pikachu")
    while True:
        play = input("Estas pensando en un pokemon  ?\n")
        if  play == 'no':
            print('ta bien \n')
            print(json.dumps(raiz, default=lambda obj: obj.__dict__))
            with open("pokemon.txt", "w") as file:
                file.write(json.dumps(arbol, default=lambda obj: obj.__dict__))
            break
        arbol = raiz
        while arbol.no != None:
            respuesta = input(arbol.dato + ' ?\n')
            if respuesta == 'si':
                arbol = arbol.si
            elif respuesta == 'no':
                arbol = arbol.no
            else:
                print('no entendi :( si o no?\n')
        # adivinar
        pokemon = arbol.dato
        if input("Es un " + pokemon + " ?\n") == 'si':
            print('Lo sabia ;)\n')
            continue
        # ******************Nuevo Pokemon*************
        nuevo = input("Me rindo :( \n En que pokemon pensabas ?\n")
        info = input('Y que tiene un ' + nuevo + ' de diferente respecto a ' + pokemon + '?\n')
        arbol.dato = info
        arbol.si = Arbol(nuevo)
        arbol.no = Arbol(pokemon)
if __name__ == '__main__':
    main()
