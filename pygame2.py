# # version 1 Uni celula
# import copy
# import os
# import time
# import platform  # Added platform module for cross-platform clear

# def inicializador_tablero(filas, columnas):
#     # Inicializar el tablero con una célula viva en el centro
#     tablero = [[0] * columnas for _ in range(filas)]
#     centro_fila, centro_columna = filas // 2, columnas // 2
#     tablero[centro_fila][centro_columna] = 1
#     return tablero

# def imprimir_tablero(tablero):
#     for fila in tablero:
#         print(' '.join(['🦠' if celda else ' ' for celda in fila]))

# def contar_vecinos(tablero, fila, columna):
#     filas, columnas = len(tablero), len(tablero[0])
#     vecinos = [
#         (fila + i, columna + j)
#         for i in range(-1, 2)
#         for j in range(-1, 2)
#         if i != 0 or j != 0
#     ]
#     contar = 0
#     for f, c in vecinos:
#         if 0 <= f < filas and 0 <= c < columnas and tablero[f][c] == 1:
#             contar += 1
#     return contar

# def evolucionar(tablero, generacion_actual):
#     nuevo_tablero = copy.deepcopy(tablero)
#     filas, columnas = len(tablero), len(tablero[0])

#     for fila in range(filas):
#         for columna in range(columnas):
#             vecinos_vivos = contar_vecinos(tablero, fila, columna)

#             if tablero[fila][columna] == 1:  # Célula viva
#                 if vecinos_vivos < 2 or vecinos_vivos > 3:
#                     nuevo_tablero[fila][columna] = 0  # Muere por subpoblación o superpoblación
#             else:  # Célula muerta
#                 if vecinos_vivos == 3:
#                     nuevo_tablero[fila][columna] = 1  # Revive por reproducción

#     return nuevo_tablero

# if __name__ == "__main__":
#     filas, columnas = 25, 50
#     tablero = inicializador_tablero(filas, columnas)

#     generaciones = 0
#     while True:
#         os.system('cls' if platform.system() == 'Windows' else 'clear')  # Use platform module for cross-platform clear
#         imprimir_tablero(tablero)
#         tablero = evolucionar(tablero, generacion_actual=generaciones)
#         time.sleep(0.5)  # Ajusta el tiempo de espera según tus preferencias

# version 2
# import random
# import copy
# import os
# import time
# import platform  # Added platform module for cross-platform clear

# def inicializador_tablero(filas, columnas, probabilidad_vida=0.2):
#     return [[1 if random.random() < probabilidad_vida else 0 for _ in range(columnas)] for _ in range(filas)]

# def imprimir_tablero(tablero):
#     for fila in tablero:
#         print(' '.join(['■' if celda else '□' for celda in fila]))

# def contar_vecinos(tablero, fila, columna):
#     filas, columnas = len(tablero), len(tablero[0])
#     vecinos = [
#         (fila + i, columna + j)
#         for i in range(-1, 2)
#         for j in range(-1, 2)
#         if i != 0 or j != 0
#     ]
#     contar = 0
#     for f, c in vecinos:
#         if 0 <= f < filas and 0 <= c < columnas and tablero[f][c] == 1:
#             contar += 1
#     return contar

# def evolucionar(tablero, generacion_actual):
#     nuevo_tablero = copy.deepcopy(tablero)
#     filas, columnas = len(tablero), len(tablero[0])

#     for fila in range(filas):
#         for columna in range(columnas):
#             vecinos_vivos = contar_vecinos(tablero, fila, columna)

#             if tablero[fila][columna] == 1:  # Célula viva
#                 if vecinos_vivos < 2 or vecinos_vivos > 3:
#                     nuevo_tablero[fila][columna] = 0  # Muere por subpoblación o superpoblación
#                 elif generacion_actual - tablero[fila][columna] > 10:
#                     nuevo_tablero[fila][columna] = 'X'  # Cambia a 'X' after 10 generations
#             else:  # Célula muerta
#                 if vecinos_vivos == 3:
#                     nuevo_tablero[fila][columna] = 1  # Revive por reproducción

#     return nuevo_tablero



# if __name__ == "__main__":
#     filas, columnas = 25, 50
#     tablero = inicializador_tablero(filas, columnas)

#     generaciones = 0
#     # for _ in range(generaciones):
#     while True:
#         os.system('cls' if platform.system() == 'Windows' else 'clear')  # Use platform module for cross-platform clear
#         imprimir_tablero(tablero)
#         tablero = evolucionar(tablero, generacion_actual=generaciones)
#         time.sleep(0.1)
        
        
# # Version 3
# # Nueva regla Si una celula tine mas de 10 generaciones se combierte ne 🥐
# import random
# import copy
# import os
# import time
# import platform

# def inicializador_tablero(filas, columnas, probabilidad_vida=0.2):
#     return [[(1, 0) if random.random() < probabilidad_vida else (0, 0) for _ in range(columnas)] for _ in range(filas)]

# def imprimir_tablero(tablero, generacion_actual):
#     print(f"Generación: {generacion_actual}")
#     for fila in tablero:
#         print(' '.join(['🦠' if celda[0] == 1 else ' ' if celda[0] == 0 else '🥐' if celda[0] == 2 else ' ' for celda in fila]))

# def contar_vecinos(tablero, fila, columna):
#     filas, columnas = len(tablero), len(tablero[0])
#     vecinos = [
#         (fila + i, columna + j)
#         for i in range(-1, 2)
#         for j in range(-1, 2)
#         if i != 0 or j != 0
#     ]
#     contar = 0
#     for f, c in vecinos:
#         if 0 <= f < filas and 0 <= c < columnas and (tablero[f][c][0] == 1 or tablero[f][c][0] == 2):
#             contar += 1
#     return contar


# def evolucionar(tablero, generacion_actual):
#     nuevo_tablero = copy.deepcopy(tablero)
#     filas, columnas = len(tablero), len(tablero[0])

#     for fila in range(filas):
#         for columna in range(columnas):
#             estado, generaciones = tablero[fila][columna]

#             vecinos_vivos = contar_vecinos(tablero, fila, columna)

#             if estado == 1 or estado == 2:  # Célula viva
#                 if vecinos_vivos < 2 or vecinos_vivos > 3:
#                     nuevo_tablero[fila][columna] = (0, 0)  # Muere por subpoblación o superpoblación
#                 # elif generacion_actual - generaciones >= 10:
#                 elif generaciones >= 10:
#                     nuevo_tablero[fila][columna] = (2, generacion_actual)  # Cambia a '🥐' después de 10 generaciones de vida
#                 else:
#                     nuevo_tablero[fila][columna] = (1, generaciones + 1)  # Incrementa el contador de generaciones
#             else:  # Célula muerta
#                 if vecinos_vivos == 3:
#                     nuevo_tablero[fila][columna] = (1, generacion_actual)  # Revive por reproducción

#     return nuevo_tablero




# if __name__ == "__main__":
#     filas, columnas = 25, 50
#     tablero = inicializador_tablero(filas, columnas)

#     generaciones = 0
#     while True:
#         os.system('cls' if platform.system() == 'Windows' else 'clear')
#         imprimir_tablero(tablero, generacion_actual=generaciones)
#         tablero = evolucionar(tablero, generacion_actual=generaciones)
#         generaciones += 1  # Incrementa el número de generaciones
#         time.sleep(0.1)
        
# Version 4 app 

# import random
# import copy
# import time
# import tkinter as tk

# def inicializador_tablero(filas, columnas, probabilidad_vida=0.2):
#     return [[(1, 0) if random.random() < probabilidad_vida else (0, 0) for _ in range(columnas)] for _ in range(filas)]

# def imprimir_tablero(tablero, generacion_actual, label):
#     contenido = f"Generación: {generacion_actual}\n"
#     for fila in tablero:
#         contenido += ' '.join(['🦠' if celda[0] == 1 else ' ' if celda[0] == 0 else '🥐' if celda[0] == 2 else ' ' for celda in fila]) + '\n'
#     label.config(text=contenido)

# def contar_vecinos(tablero, fila, columna):
#     filas, columnas = len(tablero), len(tablero[0])
#     vecinos = [
#         (fila + i, columna + j)
#         for i in range(-1, 2)
#         for j in range(-1, 2)
#         if i != 0 or j != 0
#     ]
#     contar = 0
#     for f, c in vecinos:
#         if 0 <= f < filas and 0 <= c < columnas and (tablero[f][c][0] == 1 or tablero[f][c][0] == 2):
#             contar += 1
#     return contar

# def evolucionar(tablero, generacion_actual):
#     nuevo_tablero = copy.deepcopy(tablero)
#     filas, columnas = len(tablero), len(tablero[0])

#     for fila in range(filas):
#         for columna in range(columnas):
#             estado, generaciones = tablero[fila][columna]

#             vecinos_vivos = contar_vecinos(tablero, fila, columna)

#             if estado == 1 or estado == 2:  # Célula viva
#                 if vecinos_vivos < 2 or vecinos_vivos > 3:
#                     nuevo_tablero[fila][columna] = (0, 0)  # Muere por subpoblación o superpoblación
#                 elif generaciones >= 10:
#                     nuevo_tablero[fila][columna] = (2, generacion_actual)  # Cambia a '🥐' después de 10 generaciones de vida
#                 else:
#                     nuevo_tablero[fila][columna] = (1, generaciones + 1)  # Incrementa el contador de generaciones
#             else:  # Célula muerta
#                 if vecinos_vivos == 3:
#                     nuevo_tablero[fila][columna] = (1, generacion_actual)  # Revive por reproducción

#     return nuevo_tablero

# def actualizar(tablero, generacion_actual, label):
#     imprimir_tablero(tablero, generacion_actual, label)
#     tablero = evolucionar(tablero, generacion_actual)
#     return tablero, generacion_actual + 1

# def iniciar_simulacion():
#     global tablero, generacion_actual
#     while True:
#         tablero, generacion_actual = actualizar(tablero, generacion_actual, tablero_label)
#         time.sleep(0.1)
#         root.update()

# # Crear la ventana principal
# root = tk.Tk()
# root.title("Juego de la Vida")
# root.configure(bg="black")  # Configurar el color de fondo a negro

# # Inicializar el tablero
# tablero = inicializador_tablero(25, 50)

# # Crear un label para mostrar el tablero
# tablero_label = tk.Label(root, text="", font=("Courier", 10), fg="white", bg="black")  # Configurar colores de texto y fondo
# tablero_label.pack()

# # Configurar el botón para iniciar la simulación
# start_button = tk.Button(root, text="Iniciar Simulación", command=iniciar_simulacion, fg="white", bg="gray")  # Configurar colores de texto y fondo
# start_button.pack()

# # Ejecutar el bucle principal de la interfaz gráfica
# generacion_actual = 0
# root.mainloop()

