import re

def parser_csv(path: str) -> list:
    lista = []
    exito = True
    try:
        with open(path,"r", encoding="utf8") as archivo:
            for linea in archivo:
                registro = re.split(",|\n",linea)
                diccionario = {}
                diccionario["titulo"] = registro[0]
                diccionario["vistas"] = registro[1]
                diccionario["duracion"] = registro[2]
                diccionario["url"] = registro[4]

                lista.append(diccionario)
    except:
        exito = False        
    return  lista



def generar_csv(path:str, lista:list):
    with open(path, "w", encoding="utf8") as archivo:
        for tema in lista:
            linea = f"{tema["titulo"]},{tema["vistas"]}{tema["duracion"]},{tema["url"]}\n"
            archivo.write(linea)

listas_temas = parser_csv("data.csv")

for tema in listas_temas:
    print(f"{tema["titulo"]}")
# print(listas_temas) 
 
otra_lista = [listas_temas[0],listas_temas[1],listas_temas[2],listas_temas[3]]  

generar_csv("copia.csv",otra_lista)        