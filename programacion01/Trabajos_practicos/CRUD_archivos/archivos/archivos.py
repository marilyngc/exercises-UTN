def lista_archivos(lista:list, path:str):

    try:
        with open(path, "w", encoding= "utf8") as archivo:
            for numeros in lista:
                archivo.write(f"{numeros}\n")
            return "Lista guardada exitosamente."
    except:
        return f"a ocurrido un error al guardar la lista en el archivo "


def parser(path:str):
    lista_multiplo_dos = []
    try:
        with open(path, "r", encoding="utf8") as archivo:
            lista_lineas = archivo.readlines()
            for linea in lista_lineas:
                numero = int(linea)
                if numero % 2 == 0:
                    lista_multiplo_dos.append(numero)         
    except:  
        return f"a ocurrido un error al generar la lista en el archivo " 
    return lista_multiplo_dos         
    
def cambio_archivo(path_principal:str, path_secundario: str): 
    try:
        with open(path_principal,"r", encoding="utf8") as archivo:
            lista_lineas = archivo.readlines()
        with open(path_secundario, "w", encoding="utf8") as segundo_archivo:
            for elemento in lista_lineas:
                segundo_archivo.write(f"{elemento}")
        return "Lista guardada"        
    except:
        return "A ocurrido un error en transferir el archivo"   
        
def contar_elementos(path:str):
    try:
        pass
    except:
        pass    
    
lista_numeros = [2, 453, 40, 5345,20,60,100]

path_origen = "programacion01\\Trabajos_practicos\\CRUD_archivos/lista_numeros.csv"
path_destino = "programacion01\\Trabajos_practicos\\CRUD_archivos/numeros_destino.csv"

guardar_lista= lista_archivos(lista_numeros, path_origen)
print(guardar_lista)

lista_con_multiplos = parser(path_origen)
print(lista_con_multiplos)

transferencia = cambio_archivo(path_origen, path_destino)
print(transferencia)
    