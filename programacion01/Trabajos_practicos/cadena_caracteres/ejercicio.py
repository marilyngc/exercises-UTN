# Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente). La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.
# Por ej:
# cadena = “murcielaguito”

def cantidad_vocales(cadena:str):
    matriz_vocal = [[0] * 2 for _ in range(5)]
    vocales = ["a","e","i","o","u"]
    contador_vocales = 0
    
    for i in range(len(cadena)):
        for j in range(len(vocales)):
            if cadena[i] == vocales[j]:
                ## guardo la vocal en la primera colmna
                matriz_vocal[j][0] = vocales[j]
                matriz_vocal[j][1] += 1
                print(vocales[j])
                contador_vocales += 1
    
    return matriz_vocal          
                
            
            
print(cantidad_vocales("murcielaguito"))            
        
# Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.