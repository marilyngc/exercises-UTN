# 1- Realizar una función recursiva que calcule la suma de los primeros números naturales:
def sumar_naturales(numero:int) -> int:
    if numero == 0:
        resultado = 0;
    else:
        resultado = numero + sumar_naturales(numero - 1);
    return resultado;

numero = 10;
suma_numeros = sumar_naturales(numero);
print(suma_numeros)



# 2- Realizar una función recursiva que calcule la potencia de un número:
def calcular_potencia(base:int, exponente:int) -> int:
    if exponente == 0 :
        resultado = 1;
    else:
        resultado = base * calcular_potencia(base,exponente - 1);
    return resultado;

base = 5;
exponente = 5;
resultado_potencia = calcular_potencia(base,exponente );
print(resultado_potencia);