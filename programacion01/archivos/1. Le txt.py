# escritura texto
# archivo = open("mi_primer_Archivo.txt","a")
# archivo.write("hola mi gente")

# archivo.close()
# print(archivo.closed)

###################
# archivo = open("mi_primer_Archivo.txt","r")
# contenido = archivo.read()

# archivo.close()
# print(contenido)

###################

# lista = ["GIO","MATI","GERMAN"]

# archivo = open("nombres.txt","w")

# for nombre in lista:
#     archivo.writelines(f"{nombre}\n")

# archivo.close()

########## administrador de contexto ############## devuelve un objeto por defecto
with open("nombre.txt","r") as archivo:
    contenido = archivo.readlines()

for nombre in contenido:
    print(nombre)
print(contenido)    
