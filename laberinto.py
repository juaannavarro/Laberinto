import pprint

laberinto_resuelto = [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]
def creaLaberinto(muro, dimLab):
    
    laberinto = []
    for i in range(dimLab):
        fila = []
        
        for j in range(dimLab):
            if ((i==j) and (i==dimLab-1)):
                fila.append('S')
            elif (tuple([i,j]) in muro):
                fila.append('X')
            else:    
                fila.append(' ')
        laberinto.append(fila)
    return laberinto


def recorreLaberinto(laberinto, numFilCol):
   
    movimientos = []
    x=y=0
    salir = False

    while not salir:
        if (x+1 < numFilCol) and (laberinto[x+1][y]!='X') and (len(movimientos) == 0 or movimientos[-1]!='Arriba'):
            movimientos.append('Abajo')
            x=x+1 
            print("Avanza Abajo posicion", x,y)
        elif (y+1 < numFilCol) and (laberinto[x][y+1]!='X') and (len(movimientos) == 0 or movimientos[-1]!='Izquierda'):

            movimientos.append('Derecha')
            y=y+1 
            print("Avanza Derecha posicion ",x,y)
        elif (y-1>0) and (y-1 < numFilCol) and (laberinto[x][y-1]!='X')and (len(movimientos) == 0 or movimientos[-1]!= 'Derecha'):
            print("Avanza Izquierda")
            movimientos.append('Izquierda')
            y=y-1       
            print("Avanza Izquierda posicion ",x,y)
        elif (x-1>0) and (x-1 < numFilCol) and (laberinto[x-1][y]!='X') and (len(movimientos) == 0 or  movimientos[-1]!= 'Abajo'):
            movimientos.append('Arriba')
            x=x-1 
            print("Avanza Arriba posicion", x,y)
        elif (x==numFilCol-1) and (y==numFilCol-1) and (laberinto[x][y]=='S'):
            salir = True
    return movimientos

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
maxFilasyColumnas=5
laberinto=creaLaberinto(muro, maxFilasyColumnas)
pprint.pprint(laberinto)

movimientos = recorreLaberinto(laberinto, maxFilasyColumnas)
print("Recorrido del laberinto", movimientos)