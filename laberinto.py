laberinto_resuelto= [
    [' ', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
    ]


hay_paso=(' ')
hay_muro=('X')
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

no_muro = ((0,0), (1,0), (1,2), (1,3), (1,4), (2,0), (2,2), (2,4), (3,0), (3,1), (3,2), (3,4))

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
print(laberinto)




Solucion=['Abajo', 'Abajo', 'Abajo', 'Abajo', 'Derecha', 'Derecha', 'Arriba', 'Arriba', 'Derecha', 'Derecha',]


while True:
    jugar=input("Movimiento hacia derecha/izquierda/arriba/abajo")