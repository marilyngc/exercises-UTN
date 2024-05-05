#martriz transpuesta
matriz = [
    [5,4,9,13],
    [9,8,7,13],
    [3,1,5,13]
]

for j in range(len(matriz[0])):#4
    for i in range(len(matriz)):#3
        print(f"{matriz[i][j]:4}",end = " ")
    print("")    
        