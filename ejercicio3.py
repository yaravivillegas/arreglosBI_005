import numpy as np
import random
'''
Crear un arreglo de dos dimensiones de tamaño 4 y 5, 
con elementos aleatorios de números enteros del 0 al 100
'''
sumaFila1 = 0
matrizz = np.zeros((4,5),dtype=int)
print(matrizz)

for i in range(4):
    for j in range(5):
        matrizz[i][j] = random.randint(0,100)
        
print(matrizz)

#Mostrar por pantalla la suma de los elementos de cada fila
for i in range(4):
    for j in range(5):
        if i == 0:
            sumaFila1 = sumaFila1 + matrizz[i][j]
            
sumaFila1Otra = matrizz[0,:].sum()    
sumaFila2 = matrizz[1,:].sum() 
sumaFila3 = matrizz[2,:].sum() 
sumaFila4 = matrizz[3,:].sum()      

print(f"fila 1: {sumaFila1} {sumaFila1Otra}")
print(f"fila 2: {sumaFila2}")
print(f"fila 3: {sumaFila3}")
print(f"fila 4: {sumaFila4}")

#Mostrar por pantalla la suma de los elementos de cada columna
            
sumaCol1 = matrizz[:,0].sum()    
sumaCol2 = matrizz[:,1].sum() 
sumaCol3 = matrizz[:,2].sum() 
sumaCol4 = matrizz[:,3].sum()    
sumaCol5 = matrizz[:,4].sum()  

print(f"columna 1: {sumaCol1}")
print(f"columna 2: {sumaCol2}")
print(f"columna 3: {sumaCol3}")
print(f"columna 4: {sumaCol4}")
print(f"columna 5: {sumaCol5}")

#Mostrar por pantalla la suma de los elementos de 
# la diagonal principal
diagonal = 0
for i in range(4):
    for j in range(5):
        if i == j:
            diagonal = diagonal + matrizz[i][j]
            
print(f"diagonal: {diagonal}")
        
#Mostrar por pantalla la cantidad de elementos impares.
print("...IMPARES...")
for i in range(4):
    for j in range(5):
        if matrizz[i][j] % 2 ==  1:
            print(matrizz[i][j])
