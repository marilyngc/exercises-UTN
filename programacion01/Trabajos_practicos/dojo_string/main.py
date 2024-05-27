"""
Consigna:
1. IMPLEMENTAR LOS METODOS VACIOS DE LA CLASE VIDEO

2. CREAR UN MENU DE USUARIO CON LAS SIGUIENTES OPCIONES:

A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización 
de videos que nos solicitan.
B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. LISTAR POR MES: el usuario ingresa un mes, y se deberán listar todos los temas lanzados en ese mes (sin importar el año)
I. SALIR 

NOTA: 
1. Las opciones BCDEFG no serán accesibles si no se normalizan previamente los datos.
2. Todas las opciones tienen que estar resueltas en metodos de la clase Video que reciban una lista de videos sumado a los
parametros necesarios para lograr el objetivo y mantener independencia de código.
"""
from os import system
from data import lista_videos
from package_strings.validate import *


seguir_menu = True
normalizados = False

while seguir_menu:
    option = input("A. NORMALIZAR OBJETOS:\n"
                   "B. MOSTRAR TEMAS\n"
                   "C. ORDENAR TEMAS\n"
                   "D. PROMEDIO DE VISTAS\n"
                   "E. MAXIMA REPRODUCCION\n"
                   "F. BUSQUEDA POR CODIGO\n"
                   "G. LISTAR POR COLABORADOR\n"
                   "H. LISTAR POR MES\n"
                   "I. Ingrese una opcion: ")
    option = option.upper()
    
    match option:
        case "A":
            for i in lista_videos:
                i.dividir_titulo()
                i.obtener_codigo_url()
                i.formatear_fecha()
               
            normalizados = True
        case "B":
            if normalizados:
                for video in range(len(lista_videos)):
                    lista_videos[video].mostrar_tema()
            else:
                print("Debes normalizar los datos")    
        case "C":
            if normalizados:
                bubble_sort(lista_videos)
            else:
                print("Debes normalizar los datos")                
        case "D":
            if normalizados:
                promedio_vistas_en_k = promedio_vistas(lista_videos)
                print(f"El promedio de visitas es: {promedio_vistas_en_k}k")
                
            else:
                print("Debes normalizar los datos")     
                           
        case "E":
            if normalizados:
                indices = maxima_reproduccion(lista_videos)
                
                for i in indices:
                    lista_videos[i].mostrar_tema()
            else:
                print("Debes normalizar los datos")       
                         
        case "F":
            if normalizados:
                indices = busqueda_por_codigo(lista_videos)
                
                for i in indices:
                    lista_videos[i].mostrar_tema()
            else:
                print("Debes normalizar los datos")  
                              
        case "G":
            if normalizados:
                nombre_ingresado = input("ingrese el nombre del colaborador")
                indices = listado_por_colaborador(lista_videos,nombre_ingresado)
                
                for i in indices:
                    lista_videos[i].mostrar_tema()         
            else:
                print("Debes normalizar los datos")                
        case "H":
            if normalizados:
                mes_ingresado = input("ingresa el mes: ")
                mes_ingresado = int(mes_ingresado)
                indices = listado_por_mes(lista_videos,mes_ingresado)
                
                for i in indices:
                    lista_videos[i].mostrar_tema()

            else:
                print("Debes normalizar los datos")                
                        
        case "I":
            seguir_menu = False        
system("pause")
system("cls")               
