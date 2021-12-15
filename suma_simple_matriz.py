from random import randint


numero_filas = int(input("Seleccione el número de filas de la matriz: "))
numero_columnas = int(input("Seleccione el número de columnas de la matriz: "))

matriz = []
for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        matriz[i].append(int(randint(0,100)))

suma = 0 

for i in range(numero_filas):
    for j in range(numero_columnas):
        suma = suma + matriz[i][j]
        suma = int(suma)

for i in range (numero_filas):
    print(matriz[i])

print(suma)

