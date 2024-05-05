print("ingresa el orden de la matriz a calcular");

filasA, columnasA = int(input()),int(input()); # 3 x 3

diagonal = 0;

if filasA == columnasA:
    #creando la matriz vacia
    matrizA = [[0] * columnasA for _ in range(filasA)]
    
    #rellenando la matriz
    print("ingrese matriz A")
    for fila in range(filasA):
        for columna in range(columnasA):
            matrizA[fila][columna] = int(input(f"ingrese la posicion numero {fila}, {columna}: "))
            
    for fila in range(len(matrizA)): #recorre fila
        for columnas in range(len(matrizA[fila])):#recorre columnas
            print(f"{matrizA[fila][columnas]:5}",end = " ")
        print("")    
    # calculando la diagonal princiál de la matriz A  
    for fila in range(filasA):
        for columna in range(columnasA):
            if fila == columna:
                diagonal += matrizA[fila][columna]      
                
              
print(f"el valor de la diagonal es: {diagonal}")                
            
    