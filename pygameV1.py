# ----------------------------version 1 Uni celula----------------------------
import copy
import os
import time
import platform 

def inicializador_tablero(filas, columnas):
    # Inicializar el tablero con una célula viva en el centro
    tablero = [[0] * columnas for _ in range(filas)]
    centro_fila, centro_columna = filas // 2, columnas // 2
    tablero[centro_fila][centro_columna] = 1
    return tablero

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(['🦠' if celda else ' ' for celda in fila]))

def contar_vecinos(tablero, fila, columna):
    filas, columnas = len(tablero), len(tablero[0])
    vecinos = [
        (fila + i, columna + j)
        for i in range(-1, 2)
        for j in range(-1, 2)
        if i != 0 or j != 0
    ]
    contar = 0
    for f, c in vecinos:
        if 0 <= f < filas and 0 <= c < columnas and tablero[f][c] == 1:
            contar += 1
    return contar

def evolucionar(tablero, generacion_actual):
    nuevo_tablero = copy.deepcopy(tablero)
    filas, columnas = len(tablero), len(tablero[0])

    for fila in range(filas):
        for columna in range(columnas):
            vecinos_vivos = contar_vecinos(tablero, fila, columna)

            if tablero[fila][columna] == 1:  # Célula viva
                if vecinos_vivos < 2 or vecinos_vivos > 3:
                    nuevo_tablero[fila][columna] = 0  # Muere por subpoblación o superpoblación
            else:  # Célula muerta
                if vecinos_vivos == 3:
                    nuevo_tablero[fila][columna] = 1  # Revive por reproducción

    return nuevo_tablero

if __name__ == "__main__":
    filas, columnas = 25, 50
    tablero = inicializador_tablero(filas, columnas)

    generaciones = 0
    while True:
        os.system('cls' if platform.system() == 'Windows' else 'clear')  
        imprimir_tablero(tablero)
        tablero = evolucionar(tablero, generacion_actual=generaciones)
        time.sleep(10)  
