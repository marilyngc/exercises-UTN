lista = [45,9,3,-3,10,-30]
############################# CALCULOS ################
suma_positivos = 0
suma_negativos = 0

for i in range(len(lista)):
    if lista[i] > 0:
        suma_positivos += lista[i]
    else:
        suma_negativos += lista[i]
            
print("numeros positivos: ", suma_positivos)            
print("numeros negativos: ", suma_negativos) 

############################# MAXIMO ################      
bandera_maximo = True

for i in range(len(lista)):
    if bandera_maximo == True or lista[i] > maximo_numero:
        maximo_numero = lista[i]
        bandera_maximo = False
        
        
 ############################# BANDERAS ################ 
bandera_negativo = False
 
for i in range(len(lista)):
    if lista[i] < 0:
        bandera_negativo = True
        break

if bandera_negativo == True:
    print("por lo menos hay un numero negativo")  
else:
    print("no hay numeros negativos")  
    
############################# buscar y reemplazar ################ 

numero_buscado = 3
reemplazo = 1000

for i in range(len(lista)):
    if lista[i] == numero_buscado:
        lista[i] = reemplazo
        break # en caso de querer cambiar la primera coincidencia, si queremos cambiar todos los 3 encuentra lo sacamos
for i in range(len(lista)):
    print(lista[i])    
               
                