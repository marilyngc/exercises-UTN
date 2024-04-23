

def sumar_positivos(lista: list) -> int|float:
    suma_positivos = False
    if type(lista) is list and len(lista) > 0:
        suma_positivos = 0
        for i in range(len(lista)):
            if lista[i] > 0:
                suma_positivos += lista[i]
    return suma_positivos            
                
############################# MAXIMO ################   
def buscar_maximo(lista:list) -> int :
    if type(lista) is list and len(lista) > 0:
        bandera_maximo = True
        for i in range(len(lista)):
            if bandera_maximo == True or lista[i] > maximo_numero:
                maximo_numero = lista[i]
                bandera_maximo = False
    return maximo_numero    
        
 ############################# BANDERAS ################ 
def buscar_negativo(lista:list) -> bool:  
    bandera_negativo = False
    for i in range(len(lista)):
        if lista[i] < 0:
            bandera_negativo = True
            break
    return bandera_negativo    

############################# buscar y reemplazar ################ 
def buscar_reemplazar(lista:list,busqueda:int,reemplazo:int) -> int:  
    bandera = False
    if type(lista) is list and type(busqueda) is int and type(reemplazo) is int:
        bandera = True
        for i in range(len(lista)):
            if lista[i] == busqueda:
                lista[i] = reemplazo
                break # en caso de querer cambiar la primera coincidencia, si queremos cambiar todos los 3 encuentra lo sacamos
    return bandera   
lista = [45,9,3,-3,10,-30]

suma = sumar_positivos(lista)
if suma != False:
    print(suma)
else:
    print("el v alor ingresado no es una lista")    
    
maximo = buscar_maximo(lista)
print(maximo)   

bandera_negativo = buscar_negativo(lista)
if bandera_negativo == True:
    print("por lo menos hay un numero negativo")  
else:
    print("no hay numeros negativos")  
    
numero_buscado = 3
reemplazo = 1000

if buscar_reemplazar(lista,3,1000):
     for i in range(len(lista)):
            print(lista[i])   
else:
    print("Hubo un error")                  
    
    
        
                