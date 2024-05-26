def validate_number ( mensaje,numero,minimo,maximo,reintentos) -> float|int|None:
    contador_intentos = 0;
    while numero < minimo or numero > maximo:
    
        print(f"intento numero: {contador_intentos}")
        numero = input(f"ERROR {mensaje} "); 
        numero = int(numero);

        if contador_intentos == reintentos:
            print("se agotaron los intentos");
            return None 
        
        contador_intentos +=1;

def validate_leght(minimo, maximo, caracteres,usuario,tipo):
    if tipo == True:
        if caracteres < minimo or caracteres > maximo:
            print("tiene que estar entre 6 y 12 caracteres");
            usuario = input("ingrese el nombre de usuario"); 
            caracteres = len(usuario);
            tipo = usuario.isalnum();

