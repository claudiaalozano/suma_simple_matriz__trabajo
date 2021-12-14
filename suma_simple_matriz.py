numero_filas = print(input("Seleccione el número de filas de la matriz: "))
numero_columnas = print(input("Seleccione el número de columnas de la matriz: "))

matriz = []

for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        matriz[i].append(None)