  
############ CANTIDAD DE LOS POSITIVOS Y NEGATIVOS ENCONTRADOS #################            
def cantidad_positivos_negativos(lista:list):
    cantidad_positivos = 0
    cantidad_negativos = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            cantidad_positivos += 1
        else:
            cantidad_negativos += 1      
   
    return cantidad_positivos,cantidad_negativos                 

############# SUMA LOS PARES ######################  
def suma_pares(lista:list):
    suma_par = 0;
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            suma_par += lista[i]        
    return suma_par  

############ BUSCAR EL NUMERO IMPAR MAS GRANDE ##################
def mayor_impar(lista:list) -> int:
    contador_impar = 0;
    impar_mayor = 0
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            if contador_impar == 0 or lista[i] > impar_mayor:
                impar_mayor = lista[i]
                contador_impar = 1
    return impar_mayor       


################### CREA LISTA DE PARES #####################
def lista_pares(lista:list) -> list:
    pares = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares += [lista[i]]
    return pares    

################ CREA LISTA DE LAS POSICIONES IMAPRES ##################
def len_impares(lista:list) -> list:
    impares = []
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            impares += [i]
    return impares        
        
    
