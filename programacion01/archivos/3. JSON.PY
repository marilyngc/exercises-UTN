import json 

# diccionario_uno = {"nombre":"juan","edad":"25"}
# diccionario_dos = {"nombre":"maria","edad":"30"}
# diccionario_tres = {"nombre":"luis","edad":"39"}

# lista = [diccionario_uno, diccionario_dos, diccionario_tres]

# data = {} # clave del diccionario

# data["personas"] = lista

# with open("personas.json","w") as archivo:
#     json.dump(data,archivo, indent= 4)
    
    
    
with open("personas.json","r") as archivo:
    data = json.load(archivo)
    
lista_personas = data["personas"]    

print(lista_personas[0])