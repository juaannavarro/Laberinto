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
    # Bucle para añadir las filas
    for i in range(dimLab):
        fila = []
        #Bucle para añadir las columnas
        for j in range(dimLab):
            if ((i==j) and (i==dimLab-1)):
                fila.append('S')
            elif (tuple([i,j]) in muro):
                fila.append('X')
            else:    
                fila.append(' ')
        laberinto.append(fila)
    return laberinto
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
maxFilasyColumnas=5
laberinto_resuelto=creaLaberinto(maxFilasyColumnas, muro)
pprint.pprint(laberinto_resuelto)