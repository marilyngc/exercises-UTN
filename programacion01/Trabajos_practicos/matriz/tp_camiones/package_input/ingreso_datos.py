from validaciones import validate_number,validate_file,validate_posicion

def get_int(mensaje:str, minimo:int, maximo:int, reintentos:int) -> int|None:
    numero = input(mensaje)
    numero = int(numero)
    
    if type(numero) is int:
        return validate_number(mensaje,numero,minimo,maximo,reintentos)
    else:
        print("ERROR: tiene que ser un numero entero")   
        return None
        

def get_driver(mensaje:str,matrix:list) -> int|None:
    legajo = input(mensaje)
    legajo = int(legajo)
    
    if type(legajo) is int and type(matrix) is list:
        validate_file(legajo,matrix)
        return legajo
    return None     


def get_value(mensaje:str,minimo,maximo) -> int:
    validacion_entero = get_int(mensaje, minimo,maximo, 3)
    
    if validacion_entero is None:
        print("ERROR: El valor ingresado no es válido.")
        return get_value(mensaje)
    else:
        return validacion_entero
            
            
def get_matriz(matriz:list,linea,bus,recaudacion):
    retorno_matriz = validate_posicion(matriz,linea,bus,recaudacion)     
    for i in range(len(retorno_matriz)):
        for j in range(len(retorno_matriz[i])):
            return print(retorno_matriz[i][j], end=" ")
    print(" ")  
    

        
        
    
    
    

               

    

# def get_collection(mensaje:str,matrix:list,numero:int) -> int|float:
#     numero = input(mensaje)
#     numero = int(numero)
    
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
            
            
            
            
    