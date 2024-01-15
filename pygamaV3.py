# ----------------------------Version 3----------------------------
# # Nueva regla Si una celula tine mas de 10 generaciones se combierte ne 🥐
import random
import copy
import os
import time
import platform

def inicializador_tablero(filas, columnas, probabilidad_vida=0.2):
    return [[(1, 0) if random.random() < probabilidad_vida else (0, 0) for _ in range(columnas)] for _ in range(filas)]

def imprimir_tablero(tablero, generacion_actual):
    print(f"Generación: {generacion_actual}")
    for fila in tablero:
        print(' '.join(['🦠' if celda[0] == 1 else ' ' if celda[0] == 0 else '🥐' if celda[0] == 2 else ' ' for celda in fila]))

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
        if 0 <= f < filas and 0 <= c < columnas and (tablero[f][c][0] == 1 or tablero[f][c][0] == 2):
            contar += 1
    return contar


def evolucionar(tablero, generacion_actual):
    nuevo_tablero = copy.deepcopy(tablero)
    filas, columnas = len(tablero), len(tablero[0])

    for fila in range(filas):
        for columna in range(columnas):
            estado, generaciones = tablero[fila][columna]

            vecinos_vivos = contar_vecinos(tablero, fila, columna)

            if estado == 1 or estado == 2:  # Célula viva
                if vecinos_vivos < 2 or vecinos_vivos > 3:
                    nuevo_tablero[fila][columna] = (0, 0)  # Muere por subpoblación o superpoblación
                # elif generacion_actual - generaciones >= 10:
                elif generaciones >= 10:
                    nuevo_tablero[fila][columna] = (2, generacion_actual)  # Cambia a '🥐' después de 10 generaciones de vida
                else:
                    nuevo_tablero[fila][columna] = (1, generaciones + 1)  # Incrementa el contador de generaciones
            else:  # Célula muerta
                if vecinos_vivos == 3:
                    nuevo_tablero[fila][columna] = (1, generacion_actual)  # Revive por reproducción

    return nuevo_tablero




if __name__ == "__main__":
    filas, columnas = 20, 20
    tablero = inicializador_tablero(filas, columnas)

    generaciones = 0
    while True:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        imprimir_tablero(tablero, generacion_actual=generaciones)
        tablero = evolucionar(tablero, generacion_actual=generaciones)
        generaciones += 1  # Incrementa el número de generaciones
        time.sleep(0.5)
        