# Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total tiene 15 choferes (cada uno con un legajo distinto generado aleatoriamente).
# Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
# Menú:
# Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos). Si el chofer existe cargará la recaudación del viaje indicando línea y coche (no necesariamente un chofer está asignado a una única línea y coche), estos datos deben estar validados. Un chofer puede cargar más de una recaudación por día (para distintas líneas y distintos coches). Cada coche de cada línea puede tener varias recaudaciones diarias.
# Mostrar la recaudación de cada coche y línea.
# Calcular y mostrar recaudación por línea.
# Calcular y mostrar recaudación por coche. 
# Calcular y mostrar la recaudación total.
# Salir
# Todo el desarrollo tiene que estar modularizado: ingreso de datos, validaciones de líneas y coches, generación y verificación de existencia de legajo, cálculos, etc.
from os import system
import random
from package_input.ingreso_datos import get_driver,get_value,get_matriz

# Crear la matriz inicializada con -1
matriz_legajo = [[0] * 5 for _ in range(3)]
# Crear la matriz de linea y coche
matriz_linea_coche = [[0] * 3 for _ in range(5)]

bandera_seguir = True
numero_ingresado = False
# Asignar valores aleatorios a cada elemento
for i in range(len(matriz_legajo)):
    for j in range(len(matriz_legajo[i])):
        matriz_legajo[i][j] = random.randrange(100, 500)

# Imprimir la matriz
for i in range(len(matriz_legajo)):
    for j in range(len(matriz_legajo[i])):
        print(matriz_legajo[i][j], end=" ")
    print("")



while bandera_seguir:
    opcion = int(input("1- ingresar su legajo\n2- ingresar linea y coche\n3- cargar recaudacion\n5- salir\nelija una opcion "))
    
    if numero_ingresado == False:
        match opcion:
            case 1 :
                pass
            case 2|3|4:
                print("ERROR: tiene que ingresar su legajo")
            case _ :
                print("ERROR: elija una opción")   
        
    match opcion:
        case 1:
            legajo_ingresado = get_driver("Ingrese su legajo: ",matriz_legajo)
            print(f"su legajo ingresado es: {legajo_ingresado}")   
            if legajo_ingresado == True:  
                numero_ingresado = True
            else:
                numero_ingresado = False    
        case 2:
            linea_ingresada = get_value("ingrese su linea: ",1,3)
            print(f"su linea ingresado es: {linea_ingresada}")
            bus_ingresado = get_value("ingrese su bus: ",1,5)
            print(f"su bus ingresado es: {bus_ingresado}")
        case 3:
            recaudacion_ingresada = get_value("ingrese su recaudacion: ",-1000,5000)
            print(f"su recaudacion es: {recaudacion_ingresada}")
            mostrar_matriz = get_matriz(matriz_linea_coche,linea_ingresada,bus_ingresado,recaudacion_ingresada)
            print(f"la matriz de recaudacion es: {mostrar_matriz}")
        case 4:
            pass
        case 5:
            seguir = input("desea seguir? si / no")
            if seguir == "si":
                bandera_seguir = False
            else:
                bandera_seguir = True
                            
system("pause")
system("cls")             
    


    
    