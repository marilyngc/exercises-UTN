matriz = [
    [5,4,9],
    [9,8,7],
    [3,1,5]
]

for i in range(len(matriz)): #recorre fila
    for j in range(len(matriz[i])):#recorre columnas
        print(matriz[i][j],end = " ")
    print("")    