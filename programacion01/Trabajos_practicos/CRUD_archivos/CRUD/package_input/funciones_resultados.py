from .validaciones import *
contador_id = 1
empleados_maximos = 20



def crear_empleado(id:int):

    nombre_validado = validar_caracteres("Ingrese su nombre: ")

    apellido_validado = validar_caracteres("Ingrese su apellido: ")

    dni_validado = get_int("El DNI tiene que ser mayor a 5.000.000",5000000, 100000000, 3 )
        
    puesto_validado = validar_puesto("Ingrese su puesto: ")

    salario_validado = get_int("Ingrese su salario mayor a $234.315: ", 234314,100000000, 3)

    if None in[nombre_validado, apellido_validado, dni_validado, puesto_validado, salario_validado]:
         return None
        
    else:
        empleado_creado = {"id":id, "nombre":nombre_validado, "apellido":apellido_validado, "dni":dni_validado, "puesto":puesto_validado, "salario":salario_validado}

        return empleado_creado

def agregar_empleado(empleados):

    if len(empleados) < empleados_maximos + 1:
        global contador_id
        empleado_creado = crear_empleado(contador_id)
        if empleado_creado is None:
            return "Se detectó un error al ingresar los datos. Vuelve a intentarlo."
            
        empleados.append(empleado_creado)
        contador_id += 1
        return "Empleado creado exitosamente"
    else:
        return "ERROR: no se puede agregar mas de 20 empleados"   

def buscar_empleado(diccionario:dict):
    id_ingresado = int(input("Ingrese su ID: "))  
    id_encontrado = validar_id(id_ingresado, diccionario)
    while id_encontrado is None:
        print(f"ERROR: no se encontró el id con el numero: {id_ingresado}")
        id_ingresado = int(input("Ingrese su ID: "))  
        id_encontrado = validar_id(id_ingresado) 

    return id_encontrado
        
            
def menu_modificar_empleado(id_empleado):
    bandera_seguir = True
    
    while bandera_seguir:
        opcion = int(input("1. Ingresar nombre a cambiar\n2. Ingrese apellido a cambiar\n3. ingrese DNI a cambiar\n4.Ingrese puesto a cambiar\n5.Ingrese salario a cambiar: \n6.salir\n elija una opcion:"))
        
        match opcion:
            case 1:
                nombre_ingresado = input("Ingrese el nombre: ")
                nombre_validado = validar_caracteres(nombre_ingresado)
                
                id_empleado["nombre"] = nombre_validado    
            case 2:
                apellido_ingresado = input("Ingrese el apellido")
                apellido_validado = validar_caracteres(apellido_ingresado)

                id_empleado["apellido"] = apellido_validado
            case 3:
                dni_validado = get_int("El DNI tiene que ser mayor a 5.000.000",5000000, 100000000, 3 )

                id_empleado["dni"] = dni_validado
            case 4:
                puesto_ingresado = input("Ingrese el puesto")
                puesto_validado = validar_puesto(puesto_ingresado)
                id_empleado["puesto"] = puesto_validado
            case 5:
                salario_validado = get_int("Ingrese su salario mayor a $234.315: ", 234314,100000000, 3)

                id_empleado["salario"] = salario_validado          

            case 6:
                seguir = input("seguro que quieres salir?")
                if seguir == "si":
                    print("Cambios guardados con exito")
                    bandera_seguir = False        
                else:
                    bandera_seguir = True  
            case _:
                print("ERROR: elija una opcion")

def eliminar_empleado(id:int,diccionario:dict):
    for empleado in diccionario:
        if empleado["id"] == id:
            diccionario.remove(empleado)
            return "Empleado eliminado de forma exitosa"
        
def mostrar_empleados(diccionario:dict):
    print("*" * 60)
    print(f"| {"nombre":<12} | {"apellido":<12} | {"puesto":<12} | {"salario":<12} |")
    print("_" * 60)
    
    for empleado in diccionario:
        nombre = empleado["nombre"] 
        apellido = empleado["apellido"] 
        puesto = empleado["puesto"] 
        salario = empleado["salario"] 
        print(f"| {nombre:<12} | {apellido:<12} | {puesto:<12} | ${salario:<12} |")
    
    print("*" * 60)    

def salario_promedio(diccionario:dict):
    suma_salarios = 0
    contador_salario = 0
    for salario in diccionario:
        suma_salarios += salario["salario"]
        contador_salario += 1
    
    promedio = suma_salarios / contador_salario  
    return promedio  

def dni_empleado(diccionario:dict):
    dni_ingresado = int(input("Ingrese el dni a buscar: "))
    dni_validado = validar_busqueda_dni(diccionario, dni_ingresado)
    
    for clave,valor in dni_validado.items():
        print(f"{clave} --> {valor}")
        
def ordenar_ascendiente(diccionario:dict,clave:str):
    for i in range(len(diccionario) - 1):
        for j in range(i + 1, len(diccionario)):
            if diccionario[i][clave] > diccionario[j][clave]:
                diccionario[j], diccionario[j + 1] =  diccionario[j + 1], diccionario[j]
                
def ordenar_descendiente(diccionario:dict,clave:str):
    for i in range(len(diccionario) - 1):
        for j in range(i + 1, len(diccionario)):
            if diccionario[i][clave] < diccionario[j][clave]:
                diccionario[i], diccionario[j] =  diccionario[j], diccionario[i]
                        
def menu_ordenar_empleados(diccionario:dict):
    bandera_seguir = True
    
    while bandera_seguir:
        opcion = int(input("1. ordenar por nombre ascendiente\n2. ordenar por nombre descendiente\n3. ordenar por apellido ascendiente \n4. ordenar por apellido descendiente\n5. ordenar por salario ascendiente\n6. ordenar por salario descendiente\n7.salir\n elija una opcion:"))
        
        match opcion:
            case 1:
                ordenar_nombres = ordenar_ascendiente(diccionario, "nombre")
                mostrar_empleados(diccionario)
            case 2:
                ordenar_nombres = ordenar_descendiente(diccionario, "nombre")
                mostrar_empleados(diccionario)
            case 3:
                ordenar_apellido = ordenar_ascendiente(diccionario, "apellido")
                mostrar_empleados(diccionario)
            case 4:
                ordenar_apellido = ordenar_descendiente(diccionario,"apellido")
                mostrar_empleados(diccionario)
            case 5:
                ordenar_salario = ordenar_ascendiente(diccionario,"salario")
                mostrar_empleados(diccionario)
            case 6:
                ordenar_salario = ordenar_ascendiente(diccionario,"salario")
                mostrar_empleados(diccionario)

            case 7:
                seguir = input("seguro que quieres salir?")
                if seguir == "si":
                    print("Cambios guardados con exito")
                    bandera_seguir = False        
                else:
                    bandera_seguir = True  
            case _:
                print("ERROR: elija una opcion")
    
    
    
        
            