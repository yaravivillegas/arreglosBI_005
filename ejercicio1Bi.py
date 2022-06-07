'''
 Crear un arreglo de dos dimensiones de tamaño 3 x 3, 
 con elementos aleatorios de números enteros del 0 al 100.
'''
import numpy as np
import random
print("Bienvenidos a la bidimensión")
print ('Hola!, Soy Nugmar')

matriz = np.diag([1,1,1])
print(matriz)

for i in range(3):
    for j in range(3):
        matriz[i][j] = random.randint(0,100)
        
print(matriz)
print("Chao pescao")