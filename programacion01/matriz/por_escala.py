matriz = [
    [5,4,9],
    [9,8,7],
    [3,1,5]
]

escalar = 5
M = len(matriz) #filas
N = len(matriz[0]) #columnas

matriz_resultado = [[0] * N for _ in range(M)]

for i in range(M):
    for j in range(N):
        matriz_resultado[i][j] = matriz[i][j] * escalar
        
for i in range(M):
    for j in range(N):
        print(f"{matriz_resultado[i][j]:5}",end = " ")
    print("")    
                


    