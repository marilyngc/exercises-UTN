# UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, que promete revolucionar el mercado.

# Las posibles aplicaciones son las siguientes:
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA),
# Internet de las cosas (IOT)

# Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

# A) Los datos a ingresar por cada empleado encuestado son:
# nombre del empleado
# edad (no menor a 18)
# género (Masculino - Femenino - Otro)
# tecnologia (IA, RV/RA, IOT)  
# B) Cargar por terminal 10 encuestas.
# C) Determinar:
# Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
# Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
# Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.

contador = 0;
contador_m = 0;
contador_f = 0;
contador_otro = 0;

contador_m_iot_ia  = 0;
contador_no_votados_ia = 0;


for i in range(0,10):
    nombre_ingresado = input("ingrese su nombre: ");
    
    edad_ingresada = input("ingrese su edad: ");
    edad_ingresada = int(edad_ingresada);
    while edad_ingresada < 18:
        print("Tiene que ser mayor de edad");
        edad_ingresada = input("ingrese su edad: ");
        edad_ingresada = int(edad_ingresada);  
      
    tecnologia_ingresada = input("ingrese la tecnologia IA, RV/RA, IOT ");
    while tecnologia_ingresada != "IA" and tecnologia_ingresada != "RV/RA" and tecnologia_ingresada != "IOT":
        print("ingrese IA RV/RA o IOT");                     
        tecnologia_ingresada = input("ingrese la tecnologia IA, RV/RA, IOT ");  

    genero_ingresado = input("ingrese su genero M, F, Otro: ");        
    match genero_ingresado:
        case "M": 
            contador_m += 1; 
            if contador_m == 1 :
                nombre_masculino_mayor = nombre_ingresado;
                tecnologia_elegida_mayor = tecnologia_ingresada;
                edad_masculino_mayor = edad_ingresada;
            else:
                if edad_masculino_mayor < edad_ingresada:
                    nombre_masculino_mayor = nombre_ingresado;
                    tecnologia_elegida_mayor = tecnologia_ingresada;
                    edad_masculino_mayor = edad_ingresada;                       
            if tecnologia_ingresada == "IOT" or tecnologia_ingresada == "IA":
                if edad_ingresada > 24 or edad_ingresada < 51:
                    contador_m_iot_ia += 1;  
                           
        case "F":  
            contador_f += 1;  
        case "Otro": 
            contador_otro += 1;   
        case _:   
            print("el genero tiene que ser masculino, femenino o otro");
            genero_ingresado = input("ingrese su genero M, F, Otro: ");  
    
    match tecnologia_ingresada:
        case "IOT" | "RV/RA":
            if genero_ingresado != "F":
                if edad_ingresada > 32 or edad_ingresada < 41:
                    contador_no_votados_ia += 1;
    
    contador += 1;    


porcentaje_no_votados_ia =  (contador_no_votados_ia * 100 ) / contador;     

print(f"cantidad de empleados masculinos que votaron IOT o IA:  {contador_m_iot_ia}");              
print(f"Porcentaje de empleados que no votaron por IA :  {porcentaje_no_votados_ia}");              
print(f"Nombre y tecnología que votó, de los empleados de género masculino :  {nombre_masculino_mayor} {tecnologia_elegida_mayor}");              
            
            

            
                             
   
    
