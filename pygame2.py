import random
import copy
import os
import time
import platform  # Added platform module for cross-platform clear

def inicializador_tablero(filas, columnas, probabilidad_vida=0.2):
    return [[1 if random.random() < probabilidad_vida else 0 for _ in range(columnas)] for _ in range(filas)]

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(['■' if celda else '□' for celda in fila]))

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
                elif generacion_actual - tablero[fila][columna] > 10:
                    nuevo_tablero[fila][columna] = 'X'  # Cambia a 'X' after 10 generations
            else:  # Célula muerta
                if vecinos_vivos == 3:
                    nuevo_tablero[fila][columna] = 1  # Revive por reproducción

    return nuevo_tablero



if __name__ == "__main__":
    filas, columnas = 25, 50
    tablero = inicializador_tablero(filas, columnas)

    generaciones = 0
    # for _ in range(generaciones):
    while True:
        os.system('cls' if platform.system() == 'Windows' else 'clear')  # Use platform module for cross-platform clear
        imprimir_tablero(tablero)
        tablero = evolucionar(tablero, generacion_actual=generaciones)
        time.sleep(0.01)
