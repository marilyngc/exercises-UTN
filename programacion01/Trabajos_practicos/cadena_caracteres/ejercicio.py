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
                # print(vocales[j])
                contador_vocales += 1
    
    return matriz_vocal          
                 
print(cantidad_vocales("murcielaguito"))            
        
# Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.
def indice_caracter(cadena:str,caracter:str):
 
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            return i
    return -1

print(indice_caracter("hola","a"))    

# 3)Crear una función que reciba como parámetro una cadena y determine si la misma es o no un palíndromo. Deberá retornar un valor booleano indicando lo sucedido.        
def polindromo(cadena:str) -> bool:
    cadena_invertida = cadena[::-1]
    if cadena == cadena_invertida:
        return True
    else:
        return False
    
print(polindromo("anilina"))    
    
    
# 4)Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos.
# 	Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.
def caracteres_suprimidos(cadena:str) -> str:
    resultado = ""
    for i in range(len(cadena)):
        encontrado = False
        for j in range(i + 1,len(cadena)):
            if cadena[i] == cadena[j]:
                encontrado = True
                break
        if encontrado is False:
            resultado += cadena[i]    
    return resultado

print(caracteres_suprimidos("hooola"))    
# print(caracteres_suprimidos("aaabbbccc"))  
# print(caracteres_suprimidos("programación"))  

# 5)Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.     
def vocales_suprimidas(cadena:str) -> str:
    vocales = ["a","e","i","o","u"]
    resultado = ""
    for i in range(len(cadena)):
        encontrado = False
        for j in range(len(vocales)):
            if cadena[i] == vocales[j]:
                encontrado = True
                break
        
        if encontrado is False:
            resultado += cadena[i]
    return resultado

print(vocales_suprimidas("quesoquesito"))        
            
            
# 6)Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.
# Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.
def contador_subcadena(cadena:str,subcadena:str) -> int:
    contador_cadena = 0
    for i in range(len(cadena) - len(subcadena) + 1):
        subcadena_actual = cadena[i:i + len(subcadena)]
        if subcadena_actual == subcadena:
            contador_cadena += 1
    return contador_cadena        
        
print(contador_subcadena("el pan del panadero","pan"))        
    
    
    
                
                    
        
    
                