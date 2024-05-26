from os import system
from package_input.input import get_int
from package_array.Arrays_generales import *

bandera_Seguir = True
bandera_numeros_ingresados = False
lista_numeros_ingresados = [0] * 5

while bandera_Seguir:
    opcion = int(input("1. infresar datos\n2.Mostrar la cantidad de números positivos y negativos\n3.Mostrar la sumatoria de los números pares.\n4.Informar el mayor de los números impares.r\n5.Listar todos los números ingresados.\n6.Listar todos los números pares\n7.Listar los números de las posiciones impares.\n8.salir\n elija una opcion:"))

########### VERIFICAR QUE HAYA INGRESADO LOS DATOS #########
    if bandera_numeros_ingresados == False:
        match opcion:
            case 1:
                pass
            case 2|3|4|5|6|7:
                print("ERROR: debe ingresar los numeros primero")
            case _ :
                print("ERROR: elija una opción")    
                
    match opcion:
        case 1:
            for i in range(len(lista_numeros_ingresados)):
                lista_numeros_ingresados[i] = get_int("ingresa un numero",-1000,1000,2)
            bandera_numeros_ingresados = True
        case 2:
                cantidad_positivos, cantidad_negativos = cantidad_positivos_negativos(lista_numeros_ingresados)
                print("numeros positivos: ", cantidad_positivos)            
                print("numeros negativos: ", cantidad_negativos) 
        case 3:
                resultado_par = suma_pares(lista_numeros_ingresados)
                print(f"La suma de los pares es: {resultado_par}")
        case 4:
            resultado_mayor_impar = mayor_impar(lista_numeros_ingresados)
            print(f"El mayor de los impares es: {resultado_mayor_impar}")          
        case 5:
            print(f"TODOS los numeros ingresados son: {lista_numeros_ingresados}")
           
        case 6:
            resultado_lista_pares = lista_pares(lista_numeros_ingresados)
            print(f"La lista de los numero pares es: {resultado_lista_pares}")
        case 7:
            resultado_lista_impares = len_impares(lista_numeros_ingresados)
            print(f"La lista de las posiciones de impares son : {resultado_lista_impares}")
        case 8:
            seguir = input("seguro que quieres salir?")
            if seguir == "si":
                bandera_Seguir = False        
            else:
                bandera_Seguir = True  
        case _:
            print("ERROR: elija una opcion")
                      
                
system("pause")
system("cls")               