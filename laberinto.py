def calcular_posicion(x,y,movimiento):
    
    x1=x
    y1=y
    if movimiento == 1:
        x1=x1+1
    elif movimiento==2:
        x1=x1-1
    elif movimiento==3:
        y1=y1-1
    elif movimiento==4:
        y1=y1+1
    return x1, y1

def evaluar_paso(x,y, hay_paso, hay_muro):


    return
laberinto_resuelto= [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]


hay_paso=(' ')
hay_muro=('X')
hay_muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
hay_paso = ((0,0), (1,0), (1,2), (1,3), (1,4), (2,0), (2,2), (2,4), (3,0), (3,1), (3,2), (3,4))

import pprint
laberinto = [
    ['o', 'D', 'D', 'D', 'D'], 
    ['D', 'D', 'D', 'D', 'D'],
    ['D', 'D', 'D', 'D', 'D'], 
    ['D', 'D', 'D', 'D', 'D'], 
    ['D', 'D', 'D', 'D', 'S']
    ]
jugador1=('o')
print("tu eres:", jugador1)
desconocido=('D')
print("las casillas desconocidas son:", desconocido)

import random
def tablaLaberinto(lista):
    laberinto=random.choice(lista)
    tablaLaberinto=laberinto.get(laberinto)
    return lista, laberinto

print("tabla del laberinto")
pprint.pprint(laberinto)

x=0
y=0

salir=False
movimientos=[]
while not salir:
    print("Menu")
    print("1-Abajo")
    print("2-Arriba")
    print("3-Izquierda")
    print("4-Derecha")
    

    opcion=int(input("Elige una opcion:"))
    if opcion>=1 or opcion <=4:
        print("posicion actual: ", x,y)
        x,y=calcular_posicion(x,y,opcion)
        print("Nueva posicion: ",x,y)
        if opcion==1:
            movimientos.append("abajo")
        if opcion==2:
            movimientos.append("arriba")
        if opcion==3:
            movimientos.append("izquierda")
        if opcion==4:
            movimientos.append("derecha")
    else:
        continue

        if (x>=1 or x<=4) and (y>=1 or y<=4):
            evaluar_posicion=(x,y)
        else:
            continue
        
