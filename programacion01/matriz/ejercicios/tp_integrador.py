def es_cuadrado_magico(matriz):
    M = len(matriz)
    N = len(matriz)

    if M != N:
        return False

    constante_magica = M * (M**2 + 1) // 2

    # filas y columnas
    for i in range(M):
        suma_fila = 0
        suma_columna = 0
        for j in range(M):
            suma_fila += matriz[i][j]
            suma_columna += matriz[j][i]
        if suma_fila != constante_magica or suma_columna != constante_magica:
            return False
        
    return True


# pide datos al usuario
M = int(input("Ingrese cantidad de filas: "))
N = int(input("Ingrese cantidad de columnas: "))

if M != N:
    print("La matriz no es cuadrada")
else:
    matriz = [[0] * N for _ in range(M)]

    for i in range(len(matriz)): 
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input("Ingrese un número: "))


    # verifica si es o no un cuadrado mágico :)
    if es_cuadrado_magico(matriz):
        print("La matriz ingresada SI es un cuadrado mágico")
    else:
        print("La matriz ingresada NO es un cuadrado mágico")
