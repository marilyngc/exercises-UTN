def validate_number(mensaje,numero,minimo,maximo,reintentos) -> float|int|None:
    contador_intentos = 0
    while numero < minimo or numero > maximo:
        print(f"intento numero: {contador_intentos}")
        numero = input(f"ERROR {mensaje} "); 
        numero = int(numero);        
        
        if contador_intentos == reintentos:
            print("se agotaron los intentos")
        contador_intentos += 1
    return numero    


def validate_file(legajo,matrix) -> bool:
    file_find = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if legajo == matrix[i][j]:
                file_find = True
                
    if file_find :
         print(f"A ingresado su legajo de manera correcta")
    else:
        print("No se a encontrado ningun legajo")    
                       
def validate_posicion(matriz,linea,bus,recaudacion):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i + j == (linea - 1) + (bus - 1):
                matriz[i][j] += recaudacion
                        
    return matriz    
      

                       
                
                
                
    