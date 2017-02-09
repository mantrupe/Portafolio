from Tkinter import Tk, Canvas
import tkMessageBox
import copy
#####################Inicio Ventana#################################
root = Tk()
root.wm_title("Damas de DARIO")
root.geometry("500x500")
###############Variables globales################

TableroLogico = [['@','@','@','@','@','@','@','@','@','@'],
                 ['@',0,1,0,1,0,1,0,1,'@'],
                 ['@',1,0,1,0,1,0,1,0,'@'],
                 ['@',0,1,0,1,0,1,0,1,'@'],
                 ['@',1,0,1,0,1,0,1,0,'@'],
                 ['@',0,1,0,1,0,1,0,1,'@'],
                 ['@',1,0,1,0,1,0,1,0,'@'],
                 ['@',0,1,0,1,0,1,0,1,'@'],
                 ['@',1,0,1,0,1,0,1,0,'@'],
                 ['@','@','@','@','@','@','@','@','@','@']]

Estado =  [['@','@','@','@','@','@','@','@','@','@'],
           ['@',0,-1,0,-2,0,-3,0,-4,'@'],
           ['@',-5,0,-6,0,-7,0,-8,0,'@'],
           ['@',0,-9,0,-10,0,-11,0,-12,'@'],
           ['@',0, 0,0, 0,0, 0,0, 0,'@'],
           ['@',0,0, 0, 0, 0,0,0,0,'@'],
           ['@',9,0,10,0,11,0,12,0,'@'],
           ['@',0, 5,0 ,6,0 ,7, 0,8,'@'],
           ['@',1,0,2,0 ,3,0, 4,0,'@'],
           ['@', '@', '@', '@', '@', '@', '@', '@','@','@']]

Fichas = {}
Tabs = {}
max ={}
min = {}
opciones = []
seleccionado = 0
Turno = True
move = False
MaxCor = -20
MinCor = 20
deep = 7
#########Funciones#############
def encontrar(num,estado):
    x = 0
    y = 0
    for i in estado:
        x = 0
        for j in i:
            if j == num:
                coor = (x,y)
                return coor
            x = x + 1
        y = y + 1
    return False
def cambiarTurno():
    global Turno
    if Turno:
        Turno = False
    else:
        Turno = True

def crearTablero(TableroLogico):
    x = 0
    y = 0
    for i in TableroLogico:
        x = 0
        for j in i:
            if j == 0:
                c = 'black'
            elif j == 1:
                c = 'white'

            else:
                c = 'yellow'
            position = (y,x)
            Tabs[position] = tablero.create_rectangle(x,y,x+50,y+50,fill = c,outline = 'black')
            x = x+50
        y = y + 50

def DibujarEstado(estado):
    x=0
    y=0
    for i in estado:
        x=0
        for j in i:
            if j < 0 and j > -13:
                c = 'blue'
                Fichas[j] = tablero.create_oval(x+10,y+10,x+40,y+40,fill =c,outline ='black',tag = str(j) )
            if j < -12:
                c = 'aqua'
                Fichas[j] = tablero.create_oval(x + 10, y + 10, x + 40, y + 40, fill=c, outline='black', tag=str(j))
            if j > 0 and j < 13 and j != '@':
                c = 'red'
                Fichas[j] = tablero.create_oval(x+10, y+10, x + 40, y + 40, fill=c, outline='black',tag = str(j) )
            if j > 12 and j != '@':
                c = 'orange'
                Fichas[j] = tablero.create_oval(x + 10, y + 10, x + 40, y + 40, fill=c, outline='black', tag=str(j))
            x = x+50
        y=y+50


def Sucesores(estado,migue,user):
    x = 0
    y = 0
    mach = []
    per =  []
    for i in estado:
        x=0
        for j in i:
            if j < 0 and j > -13:
                if estado[y+1][x+1] == 0:
                    mach.append((y+1,x+1))
                if estado[y+1][x+1] > 0 and estado[y+1][x+1] != '@' :
                    if estado[y+2][x+2] == 0:
                        mach.append((y+2,x+2))
                if estado[y+1][x-1] == 0:
                    mach.append((y+1,x-1))
                if estado[y+1][x-1] > 0 and estado[y+1][x-1] != '@':
                    if estado[y+2][x-2] == 0:
                        mach.append((y+2,x-2))
                migue[j]=mach
                mach = []

            if j < -12:
                yC = y
                xC = x
                b = True
                while estado[yC][xC] != '@' and b:
                    if estado[yC][xC] == 0:
                        mach.append((yC,xC))
                    yC = yC +1
                    xC = xC +1
                    if estado[yC][xC] < 0 :
                        b = False
                    if estado[yC][xC] > 0 and estado[yC][xC] != '@':
                        if estado[yC + 1][xC + 1] == 0:
                            mach.append((yC + 1, xC + 1))
                            b = False
                        else:
                            b = False
                yC = y
                xC = x
                b = True
                while estado[yC][xC] != '@'and b:
                    if estado[yC][xC] == 0:
                        mach.append((yC, xC))
                    yC = yC + 1
                    xC = xC - 1
                    if estado[yC][xC] < 0 :
                        b = False
                    if estado[yC][xC] > 0 and estado[yC][xC] != '@':
                        if estado[yC + 1][xC - 1] == 0:
                            mach.append((yC + 1, xC - 1))
                            b = False
                        else:
                            b = False
                yC = y
                xC = x
                b = True
                while estado[yC][xC] != '@' and b:
                    if estado[yC][xC] == 0:
                        mach.append((yC, xC))
                    yC = yC - 1
                    xC = xC - 1
                    if estado[yC][xC] < 0 :
                        b = False
                    if estado[yC][xC] > 0 and estado[yC][xC] != '@':
                        if estado[yC - 1][xC - 1] == 0:
                            mach.append((yC - 1, xC - 1))
                            b = False
                        else:
                            b = False
                yC = y
                xC = x
                b = True
                while estado[yC][xC] != '@' and b:
                    if estado[yC][xC] == 0:
                        mach.append((yC, xC))
                    yC = yC - 1
                    xC = xC + 1
                    if estado[yC][xC] < 0 :
                        b = False
                    if estado[yC][xC] > 0 and estado[yC][xC] != '@':
                        if estado[yC - 1][xC + 1] == 0:
                            mach.append((yC - 1, xC + 1))
                            b = False
                        else:
                            b =False

                migue[j]=mach
                mach = []

            if j > 0 and j != '@':
                if estado[y-1][x+1] == 0:
                    per.append((y-1,x+1))
                if estado[y-1][x+1] < 0 :
                    if estado[y-2][x+2] == 0:
                        per.append((y-2,x+2))
                if estado[y-1][x-1] == 0:
                    per.append((y-1,x-1))
                if estado[y-1][x-1] < 0 :
                    if estado[y-2][x-2] == 0:
                        per.append((y-2,x-2))
                user[j]=per
                per =[]

            if j > 12 and j != '@':
                yC = y
                xC = x
                b = True
                while estado[yC][xC] != '@' and b:
                    if estado[yC][xC] == 0:
                        per.append((yC, xC))
                    yC = yC + 1
                    xC = xC + 1
                    if estado[yC][xC] > 0 and estado[yC][xC] != '@':
                        b = False
                    if estado[yC][xC] < 0 and estado[yC][xC] != '@':
                        if estado[yC + 1][xC + 1] == 0:
                            per.append((yC + 1, xC + 1))
                            b = False
                        else:
                            b = False
                yC = y
                xC = x
                b = True
                while estado[yC][xC] != '@' and b:
                    if estado[yC][xC] == 0:
                        per.append((yC, xC))
                    yC = yC + 1
                    xC = xC - 1
                    if estado[yC][xC] >  0:
                        b = False
                    if estado[yC][xC] < 0 and estado[yC][xC] != '@':
                        if estado[yC + 1][xC - 1] == 0:
                            per.append((yC + 1, xC - 1))
                            b = False
                        else:
                            b = False
                yC = y
                xC = x
                b = True
                while estado[yC][xC] != '@' and b:
                    if estado[yC][xC] == 0:
                        per.append((yC, xC))
                    yC = yC - 1
                    xC = xC - 1
                    if estado[yC][xC] > 0:
                        b = False
                    if estado[yC][xC] < 0 and estado[yC][xC] != '@':
                        if estado[yC - 1][xC - 1] == 0:
                            per.append((yC - 1, xC - 1))
                            b = False
                        else:
                            b = False
                yC = y
                xC = x
                b = True
                while estado[yC][xC] != '@' and b:
                    if estado[yC][xC] == 0:
                        per.append((yC, xC))
                    yC = yC - 1
                    xC = xC + 1
                    if estado[yC][xC] > 0:
                        b = False
                    if estado[yC][xC] < 0 and estado[yC][xC] != '@':
                        if estado[yC - 1][xC + 1] == 0:
                            per.append((yC - 1, xC + 1))
                            b = False
                        else:
                            b = False

                user[j] = per
                per = []

            x=x+1
        y = y+1

def Sucesor(ficha,estado):
    dic = {}
    mach = []
    per = []
    cor = encontrar(ficha,estado)
    x = cor[0]
    y = cor[1]
    if ficha < 0 and ficha > -13:
        if estado[y + 1][x + 1] == 0:
            mach.append((y + 1, x + 1))
        if estado[y + 1][x + 1] > 0 and estado[y + 1][x + 1] != '@':
            if estado[y + 2][x + 2] == 0:
                mach.append((y + 2, x + 2))
        if estado[y + 1][x - 1] == 0:
            mach.append((y + 1, x - 1))
        if estado[y + 1][x - 1] > 0 and estado[y + 1][x - 1] != '@':
            if estado[y + 2][x - 2] == 0:
                mach.append((y + 2, x - 2))
        dic[ficha]=mach
        mach = []

    if ficha < -12:
        yC = y
        xC = x
        b = True
        while estado[yC][xC] != '@' and b:
            if estado[yC][xC] == 0:
                mach.append((yC, xC))
            yC = yC + 1
            xC = xC + 1
            if estado[yC][xC] < 0:
                b = False
            if estado[yC][xC] > 0 and estado[yC][xC] != '@':
                if estado[yC + 1][xC + 1] == 0:
                    mach.append((yC + 1, xC + 1))
                    b = False
                else:
                    b = False
        yC = y
        xC = x
        b = True
        while estado[yC][xC] != '@' and b:
            if estado[yC][xC] == 0:
                mach.append((yC, xC))
            yC = yC + 1
            xC = xC - 1
            if estado[yC][xC] < 0:
                b = False
            if estado[yC][xC] > 0 and estado[yC][xC] != '@':
                if estado[yC + 1][xC - 1] == 0:
                    mach.append((yC + 1, xC - 1))
                    b = False
                else:
                    b = False
        yC = y
        xC = x
        b = True
        while estado[yC][xC] != '@' and b:
            if estado[yC][xC] == 0:
                mach.append((yC, xC))
            yC = yC - 1
            xC = xC - 1
            if estado[yC][xC] < 0:
                b = False
            if estado[yC][xC] > 0 and estado[yC][xC] != '@':
                if estado[yC - 1][xC - 1] == 0:
                    mach.append((yC - 1, xC - 1))
                    b = False
                else:
                    b = False
        yC = y
        xC = x
        b = True
        while estado[yC][xC] != '@' and b:
            if estado[yC][xC] == 0:
                mach.append((yC, xC))
            yC = yC - 1
            xC = xC + 1
            if estado[yC][xC] < 0:
                b = False
            if estado[yC][xC] > 0 and estado[yC][xC] != '@':
                if estado[yC - 1][xC + 1] == 0:
                    mach.append((yC - 1, xC + 1))
                    b = False
                else:
                    b = False

        dic[ficha] = mach
        mach = []

    if ficha > 0 and ficha != '@':
        if estado[y - 1][x + 1] == 0:
            per.append((y - 1, x + 1))
        if estado[y - 1][x + 1] < 0:
            if estado[y - 2][x + 2] == 0:
                per.append((y - 2, x + 2))
        if estado[y - 1][x - 1] == 0:
            per.append((y - 1, x - 1))
        if estado[y - 1][x - 1] < 0:
            if estado[y - 2][x - 2] == 0:
                per.append((y - 2, x - 2))
        dic[ficha] = per
        per = []

    if ficha > 12 and ficha != '@':
        yC = y
        xC = x
        b = True
        while estado[yC][xC] != '@' and b:
            if estado[yC][xC] == 0:
                per.append((yC, xC))
            yC = yC + 1
            xC = xC + 1
            if estado[yC][xC] > 0 and estado[yC][xC] != '@':
                b = False
            if estado[yC][xC] < 0 and estado[yC][xC] != '@':
                if estado[yC + 1][xC + 1] == 0:
                    per.append((yC + 1, xC + 1))
                    b = False
                else:
                    b = False
        yC = y
        xC = x
        b = True
        while estado[yC][xC] != '@' and b:
            if estado[yC][xC] == 0:
                per.append((yC, xC))
            yC = yC + 1
            xC = xC - 1
            if estado[yC][xC] > 0:
                b = False
            if estado[yC][xC] < 0 and estado[yC][xC] != '@':
                if estado[yC + 1][xC - 1] == 0:
                    per.append((yC + 1, xC - 1))
                    b = False
                else:
                    b = False
        yC = y
        xC = x
        b = True
        while estado[yC][xC] != '@' and b:
            if estado[yC][xC] == 0:
                per.append((yC, xC))
            yC = yC - 1
            xC = xC - 1
            if estado[yC][xC] > 0:
                b = False
            if estado[yC][xC] < 0 and estado[yC][xC] != '@':
                if estado[yC - 1][xC - 1] == 0:
                    per.append((yC - 1, xC - 1))
                    b = False
                else:
                    b = False
        yC = y
        xC = x
        b = True
        while estado[yC][xC] != '@' and b:
            if estado[yC][xC] == 0:
                per.append((yC, xC))
            yC = yC - 1
            xC = xC + 1
            if estado[yC][xC] > 0:
                b = False
            if estado[yC][xC] < 0 and estado[yC][xC] != '@':
                if estado[yC - 1][xC + 1] == 0:
                    per.append((yC - 1, xC + 1))
                    b = False
                else:
                    b = False

        dic[ficha] = per
        per = []

    return dic


def comer(incio,fin):
    Ix = incio[0]
    Iy = incio[1]
    Fy = fin[0]
    Fx = fin[1]
    y = Iy
    x = Ix
    encontrado = False
    while not encontrado:
        if y == Fy and x == Fx:
            comido = (0,0)
            encontrado = True
        if y < Fy:
            y = y +1
        if y > Fy:
            y = y - 1
        if x < Fx:
            x = x +1
        if x > Fx:
            x = x - 1

        if Estado[y][x] != 0:
            comido = (y,x)
            encontrado = True

    return comido

def DibujarSucesores(actual):
    '''
    for opcion in opciones:
        tablero.itemconfig(opcion,fill = 'white')
        tablero.dtag(opcion,'suc')
    del opciones[:]
    coordenadas= tablero.find_closest(event.x, event.y)
    actual = tablero.gettags(coordenadas)
     '''
    global move, seleccionado
    op = int(actual[0])
    seleccionado = op
    move = True
    if op > 0:
        for cuadro in min[op]:
            x = cuadro[0] * 50
            y = cuadro[1] * 50
            position = (x, y)
            tag = (str(x), str(y), 'suc')
            opciones.append(Tabs[position])
            tablero.itemconfig(Tabs[position], fill='orange',tag = tag)
    '''
    else :
        for cuadro in max[op]:
            x = cuadro[0] * 50
            y = cuadro[1] * 50
            position = (x, y)
            opciones.append(Tabs[position])
            tag = (str(x),str(y),'suc')
            tablero.itemconfig(Tabs[position], fill='orange',tag = tag)
    '''

def movers(ficha,posicion):
    global Turno
    OldP = encontrar(ficha,Estado)
    print OldP
    x1 = OldP[0]
    y1 = OldP[1]
    x2 = int(posicion[0])/50
    y2 = int(posicion[1])/50
    d = (y2,x2)
    if ficha < 0:
        if max[ficha].count((y2,x2)) >= 1:
            cambiarTurno()
            print Turno
            c = comer(OldP,d)
            if c != (0,0):
                y3 = c[0]
                x3 = c[1]
                Estado[y3][x3] = 0
                cambiarTurno()
            if y2 == 8:
                global MaxCor
                MaxCor = MaxCor - 1
                ficha = MaxCor -1
            Estado[y1][x1] = 0
            Estado[y2][x2] = ficha
            tablero.delete('all')
            crearTablero(TableroLogico)
            DibujarEstado(Estado)
            Sucesores(Estado,max,min)
    if ficha > 0:
        if min[ficha].count((y2,x2)) >= 1:
            cambiarTurno()
            print Turno
            c = comer(OldP, d)
            if c != (0,0):
                y3 = c[0]
                x3 = c[1]
                Estado[y3][x3] = 0
                cambiarTurno()
            if y2 == 1:
                global MinCor
                MinCor = MinCor +1
                ficha = MinCor +1
            Estado[y1][x1] = 0
            Estado[y2][x2] = ficha
            tablero.delete('all')
            crearTablero(TableroLogico)
            DibujarEstado(Estado)
            Sucesores(Estado,max,min)

    if not Turno:
        Ficha,pos = IA(Estado)
        print "Ficha->",Ficha
        print "Posicion->",pos
        print Turno
        movers(Ficha,pos)
    '''
    #_deleteEmptySucesores(max)
    lista =[]
    for x in range(-12,-1):
        f = encontrar(x,Estado)
        lista.append(f)
    if len(max) == 0:
        tkMessageBox.showinfo("Felicidades",'Ganaste :0')
   # _deleteEmptySucesores(min)
    if len(min) == 0:
        tkMessageBox.showinfo("Sorry", 'Perdiste :(')
    '''

def UserMove(event):
    actual =tablero.find_closest(event.x, event.y)
    posicion = tablero.coords(actual)
    movers(seleccionado,posicion)

def juego(event,opciones):
    global move,seleccionado
    for opcion in opciones:
        tablero.itemconfig(opcion, fill='white')
    del opciones[:]
    coordenadas = tablero.find_closest(event.x, event.y)
    if not move:
        actual = tablero.gettags(coordenadas)
        DibujarSucesores(actual)
    else:
        move = False
        pos = tablero.coords(coordenadas)
        x = pos[0]
        y = pos[1]
        c = (x,y)
        movers(seleccionado,c)

############################################
#############Funciones de Migue#############
############################################
def IA(tablero):
    PC,US,E=dict(),dict(),dict()
    Sucesores(_prepareTablero(tablero,'@'),PC,US)
    _deleteEmptySucesores(PC)
    alfaBeta={'A':0,'B':0}
    #debug(tablero,PC,heuristica(tablero),0)#----------------
    return minMax(tablero,PC,'M',alfaBeta,0)


def minMax(tablero, jugadas, mM, ab, nivel):
    nivel = nivel + 1
    juegos = list()
    fichaF = 0
    moveF = (0,0)
    if len(jugadas) == 0:  # *
        # UPS! el juego termina aqui, revisa quien gano
        return heuristica(tablero)

    if nivel == deep:
        # Heuristica||AHORA TIENES QUE SUBIR
        if mM == 'M':
            # MAX
            val = -2000
            for ficha in jugadas:
                for movimiento in jugadas[ficha]:
                    game = createTablero(ficha, movimiento, tablero)
                    nVal = heuristica(game[0])
                    if val < nVal:
                        val = nVal
            return val
        else:
            # MIN
            val = 2000
            for ficha in jugadas:
                for movimiento in jugadas[ficha]:
                    game = createTablero(ficha, movimiento, tablero)
                    nVal = heuristica(game[0])
                    #debug(game[0], "", nVal, nivel)
                    if val > nVal:
                        val = nVal
            return val
    else:
        # Sigue creando ramas
        if mM == 'M':
            # MAX
            val = -2000
            for ficha in jugadas:
                for movimiento in jugadas[ficha]:
                    game = createTablero(ficha, movimiento, tablero)
                    juegos.append(game[0])
                    XPC, XUS, Xeat = dict(), dict(), dict()  # Estas variables no se utilizan
                    Sucesores(_prepareTablero(game[0], '@'), XPC, XUS)
                    _deleteEmptySucesores(XUS)
                    #debug(game[0], XUS, "", nivel)  # -----------------
                    nVal = minMax(game[0], XUS, 'm', ab, nivel)
                    if val < nVal:
                        val = nVal
                        fichaF = ficha
                        moveF = movimiento
            if nivel == 1:

                yF = jugadas[ficha][0][0]*50
                xF = jugadas[ficha][0][1]*50
                print "Ficha ",ficha
                print "movimiento",jugadas[ficha][0][0],",",jugadas[ficha][0][1]
                xyF = (xF,yF)
                return (ficha, xyF)
            else:
                return val
        else:
            # MIN
            val = 2000
            for ficha in jugadas:
                for movimiento in jugadas[ficha]:
                    game = createTablero(ficha, movimiento, tablero)
                    juegos.append(game[0])
                    XPC, XUS, Xeat = dict(), dict(), dict()  # Estas variables no se utilizan
                    Sucesores(_prepareTablero(game[0], '@'), XPC, XUS)
                    _deleteEmptySucesores(XPC)
                    nVal = minMax(game[0], XPC, 'M', ab, nivel)
                    if val > nVal:
                        val = nVal
                return val

def createTablero(ficha, newCoord, tablero):
    xTablero = _prepareTablero(tablero, 0)
    # Coordenadas de Destino
    y, x = newCoord[0], newCoord[1]
    xO, yO = 0, 0
    xO, yO = encontrar(ficha, tablero)
    # Coordenadas de Direccion
    xD = x - xO
    yD = y - yO

    if xD < 0:
        xD = -1
    else:
        xD = 1
    if yD < 0:
        yD = -1
    else:
        yD = 1
    f = 0
    fEat = 0
    fCrown = 0
    # Coordenadas de posible enemigo
    xE, yE = 0, 0
    xTablero[yO][xO] = 0
    while f == 0:
        # Como
        if ficha < 0:
            if xTablero[yO][xO] > 0:
                xTablero[yO][xO] = 0
                fEat = 1
                xTablero[y][x] = ficha
                f = 1
        else:
            # Come usuario
            if xTablero[yO][xO] < 0:
                xTablero[yO][xO] = 0
                fEat = 1
                xTablero[y][x] = ficha
                f = 1
        if xO == x and yO == y:
            xTablero[y][x] = ficha
            f = 1
        xO = xO + xD
        yO = yO + yD
    # Coronacion
    if ficha < 0:
        if y == 8 and ficha > -13:
            xTablero[y][x] = ficha - 20
            fCrown = 1
    else:
        if y == 1 and ficha < 13:
            xTablero[y][x] = ficha + 20
            fCrown = 1
    return (xTablero, fEat, fCrown)

def heuristica(tablero):
    xTablero = _prepareTablero(tablero, 0)
    pnts = 10
    # et -> eat, no se utiliza
    PC, US, et = dict(), dict(), dict()
    Sucesores(_prepareTablero(tablero, '@'), PC, US)
    # -------REVISA SI ALGUIEN GANO-------
    _deleteEmptySucesores(PC)
    _deleteEmptySucesores(US)
    if len(PC) == 0:
        # Gana Usuario
        return -1000
    if len(US) == 0:
        # Gana PC
        return 1000
        # -----------------------------------
    for pc in PC:
        pnts = pnts + _heuristicaPieza(encontrar(pc, xTablero), xTablero)
        pnts = pnts + 15
        if pc < (-20):
            pnts = pnts + 20
    for us in US:
        pnts = pnts - _heuristicaPieza(encontrar(us, xTablero), xTablero)
        pnts = pnts - 15
        if us > 20:
            pnts = pnts - 20
    return pnts


def _heuristicaPieza(coord, tablero):
    pnts = 0
    x, y = coord[0], coord[1]

    if tablero[y][x] > 0:
        aliado = 1
    else:
        aliado = 0  # Ficha enemiga

    # En esquina
    if (x == 1 or x == 8):
        pnts = pnts + 1
    # En orilla
    if (y == 1 or y == 8):
        pnts = pnts + 1
    if aliado == 1:
        # F I C H A    A L I A D A
        if (tablero[y][x] > -20):
            pnts = pnts + (8 - (8 - y))
        fp = 0  # bandera posicion
        if (x == 1 or x == 8):
            pnts = pnts + 1
        if (y == 1 or y == 8):
            pnts = pnts + 1
        # atras izquierda
        if (tablero[y - 1][x - 1] < 0):
            fp = 1
            pnts = pnts + 1
        # atras derecha
        if (tablero[y - 1][x + 1] < 0):
            pnts = pnts + 1
            # Respaldado por izquierda y por derecha
            if fp == 1:
                pnts = pnts + 1
        fp = 0
        # delante derecha
        if (tablero[y + 1][x - 1] < 0):
            pnts = pnts + 1
            fp = 1
        if (tablero[y + 1][x + 1] < 0):
            pnts = pnts + 1
            # Respalda 2 fichas
            if fp == 1:
                pnts = pnts + 1
        if y != 8:  # <--------------------------------------------------------------E R R O R
            if (tablero[y + 2][x] > 0):
                pnts = pnts + 1
        if y != 1:
            if (tablero[y][x] < -20 and tablero[y - 2][x] > 0):
                pnts = pnts + 1
        # ficha entre 2 enemigas
        if (tablero[y - 1][x - 1] > 0 and tablero[y + 1][x + 1] > 0):
            pnts = pnts + 1
        if (tablero[y - 1][x + 1] > 0 and tablero[y + 1][x - 1] > 0):
            pnts = pnts + 1
        # ficha con amenaza inminente
        if y != 8 and y != 1:
            if x != 8:
                if (tablero[y + 1][x + 1] > 0 and tablero[y + 2][x + 2] != 0 and tablero[y - 1][x - 1] == 0):
                    pnts = pnts - 1
            if x != 1:
                if (tablero[y + 1][x - 1] > 0 and tablero[y + 2][x - 2] != 0 and tablero[y - 1][x + 1] == 0):
                    pnts = pnts - 1
    else:
        # F I C H A    E N E M I G A
        if (tablero[y][x] < 20):
            pnts = pnts + (8 - (y - 1))
        fp = 0  # bandera posicion
        if (x == 1 or x == 8):
            pnts = pnts + 1
        if (y == 1 or y == 8):
            pnts = pnts + 1
        # atras izquierda
        if (tablero[y + 1][x - 1] > 0):
            fp = 1
            pnts = pnts + 1
        # atras derecha
        if (tablero[y + 1][x + 1] > 0):
            pnts = pnts + 1
            # Respaldado por izquierda y por derecha
            if fp == 1:
                pnts = pnts + 1
        fp = 0
        # delante derecha
        if (tablero[y - 1][x - 1] > 0):
            pnts = pnts + 1
            fp = 1
        if (tablero[y - 1][x + 1] > 0):
            pnts = pnts + 1
            # Respalda 2 fichas
            if fp == 1:
                pnts = pnts + 1
        if y != 1:
            if (tablero[y - 2][x] < 0):
                pnts = pnts + 1
        if y != 8:
            if (tablero[y][x] > 20 and tablero[y + 2][x] < 0):
                pnts = pnts + 1
        # ficha entre 2 enemigas
        if (tablero[y - 1][x - 1] < 0 and tablero[y + 1][x + 1] < 0):
            pnts = pnts + 1
        if (tablero[y - 1][x + 1] < 0 and tablero[y + 1][x - 1] < 0):
            pnts = pnts + 1
        # ficha con amenaza inminente
        if y != 8 and y != 1:
            if x != 8:
                if (tablero[y - 1][x + 1] < 0 and tablero[y - 2][x + 2] != 0 and tablero[y + 1][x - 1] == 0):
                    pnts = pnts - 1
            if x != 1:
                if (tablero[y - 1][x - 1] > 0 and tablero[y - 2][x - 2] != 0 and tablero[y + 1][x + 1] == 0):
                    pnts = pnts - 1
    return pnts


def _deleteEmptySucesores(dict):
    delete = list()
    for d in dict:
        if len(dict[d])==0:
            delete.append(d)
    for d in delete:
            dict.pop(d, None)
    for d in dict:
        x = 0
        for elem in dict[d]:
            t = dict[d][x]
            dict[d][x]=list(t)
            dict[d][x].append(-1)
            x = x+1

def _prepareTablero(tablero, f):
    # Si F 0 transforma marco a 0
    xTablero = list()
    for t in tablero:
        xTablero.append(copy.deepcopy(t))
    x, y = 0, 0
    for y in range(0, 10):
        for x in range(0, 10):
            if x == 0 or x == 9:
                xTablero[y][x] = f
            if y == 0 or y == 9:
                xTablero[y][x] = f
    return xTablero

######Tablero################
tablero = Canvas(root,width = 500,height = 500)
tablero.bind("<Button-1>", lambda event: juego(event, opciones))
tablero.pack()










######Looop Ventana############################################

crearTablero(TableroLogico)
DibujarEstado(Estado)
Sucesores(Estado,max,min)
Tk.mainloop(root)
