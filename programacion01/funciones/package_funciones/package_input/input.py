from validate import validate_number, validate_leght

def get_int(mensaje: str, minimo:int, maximo:int, reintentos: int) -> int|None:
    numero = input(mensaje);
    numero = int(numero);
    validate_number(mensaje,numero,minimo,maximo,reintentos)
  
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



edad = get_int("igrese su edad: ",18, 30, 3); # 18 - 30
edad_retorno = print(edad);

legajo = get_int("ingrese su legajo: ", 1000, 2000, 3); # 1000 - 2000mary
legajo_retorno = print(legajo);

nota = get_int("ingrese su nota: ", 1, 10, 3); # 1 - 10
nota_retorno = print(nota);


##FLOAT
edad = get_float("igrese su edad: ",18, 30, 3); # 18 - 30
edad_retorno = print(edad);

legajo = get_float("ingrese su legajo: ", 1000, 2000, 3); # 1000 - 2000
legajo_retorno = print(legajo);

nota = get_float("ingrese su nota: ", 1, 10, 3); # 1 - 10
nota_retorno = print(nota);

## String
usuario = get_string(5,13);
usuario_retorno = print(f"su usuario es:{ usuario}");

