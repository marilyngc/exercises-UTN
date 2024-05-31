import json

def parser_json(path:str) -> list:
    with open(path, "r") as archivo:
        diccionario = json.load(archivo)
        
    return diccionario["bzrp"]

mi_lista = parser_json("data.json")    

print(mi_lista)

######### crear JSON ##########
def generar_json(path:str, lista: list):
    with open(path,"w") as archivo:
        json.dump(lista,archivo, indent=4)
        
mi_lista = parser_json("data.json")    

print(mi_lista)
otra_lista = [mi_lista[0],mi_lista[1],mi_lista[2],mi_lista[3]]

diccionario = {}
diccionario ["BZRP"] = otra_lista

generar_json("copia en json.json",diccionario)
