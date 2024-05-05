def es_cuadrado_magico(matriz) -> bool:
    """Determinar si una matriz es un cuadrado mágico o no

    Args:
        matriz (_type_): Verifica mediante la constante mágica si es o no un cuadrado mágico

    Returns:
        _type_: True si es cuadrado mágico | False si NO es cuadrado mágico
    """
    # filas y columnas
    M = len(matriz)
    N = len(matriz[0])

   # variables y formula
    constante_magica = M * (M**2 + 1) / 2 
    retorno = False    
    traza = 0
    diagonal_inversa = 0
   
    for i in range(M):
        suma_fila = 0
        suma_columna = 0
    
        for j in range(N):
            # filas y columnas
            suma_fila += matriz[i][j]
            suma_columna += matriz[j][i]
            # diagonal principal
            if i == j :
                traza += matriz[i][j]
            # diagonal secundaria
            if i + j == M - 1:
                diagonal_inversa += matriz[i][j] # (0,2), (1,1) y (2,0)
    # compara la suma con la formula de la constante mágica
    if suma_fila == constante_magica and suma_columna == constante_magica and traza == constante_magica and diagonal_inversa == constante_magica:
        retorno = True

    return retorno

# pide datos al usuario
M = int(input("Ingrese la cantidad de filas: "))
N = int(input("Ingrese la cantidad de columnas: "))

while M != N:
    M = int(input("Error. Reingrese la cantidad de filas: "))
    N = int(input("Error. Reingrese la cantidad de columnas: "))

matriz = [[0] * N for _ in range(M)]
for i in range(len(matriz)): 
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Ingrese un número: {i}, {j}: "))

# verifica si es o no un cuadrado mágico
if es_cuadrado_magico(matriz):
    mensaje = "La matriz ingresada SI es un cuadrado mágico"
else:
    mensaje = "La matriz ingresada NO es un cuadrado mágico"
print(mensaje)
