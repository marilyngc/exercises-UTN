from os import system
from package_input.funciones_resultados import *

bandera_Seguir = True
empleados = []

while bandera_Seguir:
    opcion = int(input("1. Ingresar empleado\n2. Modificar empleado\n3. Eliminar empleado.\n4.Mostrar todos\n5.Calcular salario promedio: \n6.Buscar empleado por DNI: \n7.Ordenar empleados: \n8.salir\n elija una opcion:"))

    match opcion:
        case 1:
           mensaje = agregar_empleado(empleados)
           print(mensaje)
           
        case 2:
            id_empleado = buscar_empleado(empleados)
            modificacion = menu_modificar_empleado(id_empleado)
            
        case 3:
            id_empleado = buscar_empleado(empleados)
            empleado_eliminado = eliminar_empleado(id_empleado, empleados)
            print(empleado_eliminado)
            
        case 4:
            tabla_empleados = mostrar_empleados(empleados)
            
        case 5:
            resultado_promedio = salario_promedio(empleados)
            print(resultado_promedio)
           
        case 6:
            empleado = dni_empleado(empleados)
            
        case 7:
            ordenamiento = menu_ordenar_empleados(empleados)

        case 8:
            seguir = input("seguro que quieres salir?")
            if seguir == "si":
                bandera_Seguir = False        
            else:
                bandera_Seguir = True  
        case _:
            print("ERROR: elija una opcion")
                      
print(empleados)                
system("pause")
system("cls")               

