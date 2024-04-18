# from package_funciones.funciones import modificar_valor;
# from random import randint,choice;

# modificar_valor(5);



# numero = randint(1,9);

# print(numero);

# lista_opciones = ["verde","rojo","naranja"];

# opcion = choice(lista_opciones);

# print(opcion);

# import pygame;

# running = True;
# pygame.display.set_mode

def get_int(mensaje: str, minimo:int, maximo:int, reintentos: int) -> int|None:
    numero = input(mensaje);
    numero = int(numero);
    contador_intentos = 0;
    while numero < minimo or numero > maximo:
        contador_intentos +=1;
        numero = input(f"ERROR {mensaje} "); 
        numero = int(numero);
        
        if contador_intentos == reintentos:
            print("se agotaron los intentos");
            return None 
    return numero;
        
def get_float(mensaje: str, minimo:float, maximo:float, reintentos: float) -> float|None:
    numero = input(mensaje);
    numero = float(numero);
    contador_intentos = 0;
    while numero < minimo or numero > maximo:
        contador_intentos +=1;
        numero = input(f"ERROR {mensaje} "); 
        numero = float(numero);
        
        if contador_intentos == reintentos:
            print("se agotaron los intentos");
            return None 
    return numero;
        
# numero_solicitado = get_int();    

# print(f"el numero ingresado es: {numero_solicitado}");


edad = get_int("igrese su edad: ",18, 30, 3); # 18 - 30

legajo = get_int("ingrese su legajo: ", 1000, 2000, 2); # 1000 - 2000

nota = get_int("ingrese su nota: ", 1, 10, 3); # 1 - 10
