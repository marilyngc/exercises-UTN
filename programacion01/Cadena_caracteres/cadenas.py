cadena = "Hola mundo"


# for i in range(2,6): ## el 6 es exclusive
#     print(cadena[i], end="")
    
###############################################    
print(cadena[2:6])    
print(cadena[2:])
print(cadena[:6])
print(cadena[0:])
print(cadena[:])
print(cadena[:: - 1])

cadena = "p" + cadena[1:]
print(cadena)

    
    

# cadena = "hola"
# for i in range(3):
#     print(cadena,end = " ")    
#####################################
# nombres = ["luis","ana","diego","juan"]


# for i in range(0,len(nombres) - 1):
#     for j in range(i + 1,len(nombres)):
#         if nombres[i] > nombres[j]:
#             auxiliar = nombres[i]
#             nombres[i] = nombres[j]
#             nombres[j] = auxiliar
            
            
            # codigo asci

###################################
# cadena = "H3LA"    
# nueva_cadena = ""
# print(ord("H"))       
# print(chr(65)) 
# for i in range(len(cadena)):
#     orden = ord(cadena[i]) 
#     if orden >= 65 and orden <= 90:
#         caracter = chr(orden + 32)
#         nueva_cadena += caracter
#         continue
    
#     nueva_cadena += cadena[i]
# print(nueva_cadena)


# ##################
# def es_caracter_valido(un_caracter,validos):
#     es_valido = False
#     for i in range(len(validos)):
#         if un_caracter == validos[i]:
#             es_valido = True
#             break
    
#     return es_valido                    

# caracteres_validos = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" 
# cadena = "Hola"

 
    