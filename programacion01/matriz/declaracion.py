## compresion de listas

M = 4
N = 3

matriz = [[0] * N for _ in range(M)]

for i in range(len(matriz)): #recorre fila
    for j in range(len(matriz[i])):#recorre columnas
        print(matriz[i][j],end = " ")
    print("")    