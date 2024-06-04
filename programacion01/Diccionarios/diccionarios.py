mi_diccionario = {
    "nombre":"luis",
    "Edad": 19,
    "ciudad":"cordoba"
}

print(mi_diccionario["ciudad"])

## agregar key #####

mi_diccionario["profesion"] = "estudiante"


###### eliminar #####
edad = mi_diccionario.pop("Edad")


####### metodos #######
print(mi_diccionario.keys())
print(mi_diccionario.values())

##cdevuelve lista de tuplas #######
print(mi_diccionario.items())

######## recorrer diccionarios ######
for clave in mi_diccionario:
    print(mi_diccionario[clave])
    
for clave,valor in mi_diccionario.items():
    print(f"{clave} -> {valor}")    
