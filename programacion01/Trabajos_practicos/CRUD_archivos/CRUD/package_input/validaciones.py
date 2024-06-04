def validate_number(mensaje:str,numero: int | float,minimo: int | float,maximo: int | float, reintentos: int ,tipo:type) -> float|int|None:
    contador_intentos = 0
    while numero < minimo or numero > maximo:
        print(f"intento numero: {contador_intentos}")
        numero = input(f"ERROR {mensaje} "); 
        numero = tipo(numero);        
        
        if contador_intentos == reintentos:
            print("se agotaron los intentos")
        contador_intentos += 1
    return numero    
def get_int(mensaje:str, minimo:int, maximo:int, reintentos:int) -> int|None:
    try:
        numero = input(mensaje)
        numero = int(numero)

        if type(numero) is int:
            return validate_number(mensaje,numero,minimo,maximo,reintentos,int)
        else:
            print("ERROR: tiene que ser un numero entero")   
            return None
    except ValueError:
        print("ERROR: debe ingresar un número entero.")
        return None
      
# def get_float(mensaje:str, minimo:float, maximo:float, reintentos:int) -> float|None:
#     numero = input(mensaje)
#     numero = float(numero)
    
#     while type(numero) is not float:
#         print("ERROR: tiene que ser un numero decimal")
#         numero = input(mensaje)
#         numero = float(numero)
#         return get_float(mensaje,minimo,maximo,reintentos)
  
 
#     return validate_number(mensaje,numero,minimo,maximo,reintentos,float)

    
def validar_caracteres(mensaje:str) -> str:
    cadena_ingresada = input(mensaje)
    
    if len(cadena_ingresada) > 20:
        print("ERROR: tiene que tener menos de 20 caracteres")
        cadena_ingresada = input(mensaje)
        return validar_caracteres(cadena_ingresada)
    else:
        return cadena_ingresada
    
      
def validar_puesto(mensaje:str) -> str:
    puesto = input(mensaje)
    puestos_validos = ["Gerente", "Supervisor", "Analista", "Encargado"]
    for puesto in puestos_validos:
            return puesto
        
    print("ERROR: tiene que tener un puesto de “Gerente” / “Supervisor” / “Analista” / “Encargado” /  ")
    puesto = input(mensaje)
    return  validar_puesto(puesto)
        
# def validar_salario(mensaje:str) -> int:
#     salario_ingresado = float(input(mensaje))
#     salario = get_float(mensaje,234314,None,3)
    
#     if salario > 234314:
#         return salario
#     else:
#         print("ERROR: tiene que tener un salario mayor a $234.315 ")
#         salario = int(input("Ingrese su salario"))
#         return validar_salario(salario)     
    
def validar_id(id:int,diccionario:dict):
    for empleado in diccionario:
        if empleado["id"] == id:
            return empleado
       
    return None
   
def validar_busqueda_dni(diccionario:dict, dni:int):
    for empleado in diccionario:
        if empleado["dni"] == dni:
            return empleado  
        return "ERROR: no se encontró el dni solicitado"