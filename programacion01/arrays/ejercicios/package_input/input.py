from .validate import validate_number, validate_leght

def get_int(mensaje: str, minimo:int, maximo:int, reintentos: int) -> int|None:
    numero = input(mensaje);
    numero = int(numero);
   
    if type(numero) is int:
        validate_number(mensaje,numero,minimo,maximo,reintentos)
    else:
        print("ERROR: tiene que ser un numero")    
  
    return numero;
        
def get_float(mensaje: str, minimo:float, maximo:float, reintentos: float) -> float|None:
    numero = input(mensaje);
    numero = float(numero);
    validate_number(mensaje,numero,minimo,maximo,reintentos)
    return numero;
        
def get_string(minimo:int, maximo: int) -> str|None:
    usuario = input("ingrese el nombre de usuario: "); 
    caracteres = len(usuario);
    tipo = usuario.isalnum();

    validate_leght(minimo, maximo, caracteres,usuario,tipo);
    return usuario

# def encontrar_par_impar(lista:list):
#     for i in range(len(lista)):
#         if lista[i] % 2 == 0:
#             print(f"numeros PAR: {lista[i]}")
#         else:
#             print(f"numeros IMPAR: {lista[i]}")
    
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
        
    

             
                    
          

    
# edad = get_int("igrese su edad: ",18, 30, 3); # 18 - 30
# edad_retorno = print(edad);

# legajo = get_int("ingrese su legajo: ", 1000, 2000, 3); # 1000 - 2000mary
# legajo_retorno = print(legajo);

# nota = get_int("ingrese su nota: ", 1, 10, 3); # 1 - 10
# nota_retorno = print(nota);


# ##FLOAT
# edad = get_float("igrese su edad: ",18, 30, 3); # 18 - 30
# edad_retorno = print(edad);

# legajo = get_float("ingrese su legajo: ", 1000, 2000, 3); # 1000 - 2000
# legajo_retorno = print(legajo);

# nota = get_float("ingrese su nota: ", 1, 10, 3); # 1 - 10
# nota_retorno = print(nota);

# ## String
# usuario = get_string(5,13);
# usuario_retorno = print(f"su usuario es:{ usuario}");

