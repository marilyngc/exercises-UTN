from os import system
from package_input.funciones_resultados import *
from package_input.archivos import *

path_archivo = "programacion01\Trabajos_practicos\CRUD_archivos\CRUD\doumentos\Empleados.csv"
empleados = []
resultado_lectura = leer_archivos(path_archivo, empleados)
print("Empleados:", resultado_lectura)
def menu_empleados(diccionario:dict):
    bandera_Seguir = True
    while bandera_Seguir:
        opcion = int(input("1. Ingresar empleado\n2. Modificar empleado\n3. Eliminar empleado.\n4. Mostrar todos\n5. Calcular salario promedio: \n6. Buscar empleado por DNI: \n7 .Ordenar empleados: \n8. salir\n elija una opcion:"))

        match opcion:
            case 1:
               mensaje = agregar_empleado(diccionario)
               print(mensaje)

            case 2:
                id_validado = get_int("Ingrese el ID del empleado a modificar: ", 1, 20, 3)
                id_empleado = buscar_empleado_id(diccionario, id_validado)
                modificacion = menu_modificar_empleado(id_empleado)

            case 3:
                id_validado = get_int("Ingrese el ID del empleado a eliminar: ", 1, 20, 3)
                id_empleado = buscar_empleado_id(diccionario, id_validado)
                empleado_eliminado = eliminar_empleado(id_empleado, diccionario)
                print(empleado_eliminado)

            case 4:
                tabla_empleados = mostrar_empleados(diccionario)

            case 5:
                resultado_promedio = salario_promedio(diccionario)
                print(resultado_promedio)

            case 6:
                dni_validado = get_int("El DNI tiene que ser mayor a 5.000.000: ",5000000, 100000000, 3 )
                empleado = dni_empleado(diccionario, dni_validado)

            case 7:
                ordenamiento = menu_ordenar_empleados(diccionario)

            case 8:
                seguir = input("seguro que quieres salir?")
                if seguir == "si":
                    bandera_Seguir = False        
                else:
                    bandera_Seguir = True  
            case _:
                print("ERROR: elija una opcion")
                
menu_empleados(empleados)
print(empleados)                
system("pause")
system("cls")               

