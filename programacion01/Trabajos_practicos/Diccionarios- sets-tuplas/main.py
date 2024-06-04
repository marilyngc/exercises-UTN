from Grafico import *
from os import *

def inicio_programa():
    system("cls")
    while True:
        opcion = int(input("1. Seleccionar figura y cargar valores\n2. Visualizar resultados\n3. Salir\nElija una opción: "))
        match opcion:
            case 1:
                system("cls")
                print("¿Qué tipo de figura desea representar?")
                que_figura = input("a. Círculo\nb. Rectángulo\nc. Triángulo\nd. Volver al menu anterior\nElija una opción: ")
                match que_figura:
                    case "a":
                        system("cls")
                        figura = {}
                    case "b":
                        system("cls")
                        figura = {}
                    case "c":
                        system("cls")
                        figura = {}
            case 2:
                graficar(figura)
            case 3:
                print("Gracias por usar nuestro programa")
                break 
            
        system("cls")   

inicio_programa()