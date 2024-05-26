# from .package_input.input import *
# """
# 1- Realizar una función recursiva que calcule la suma de los primeros números naturales:
# """
def sumar_naturales(numero:int) -> int:
    if numero == 0:
        resultado = 0
    else:
        resultado = numero + sumar_naturales(numero - 1)
    return resultado

numero_global = 10
suma_numeros = sumar_naturales(numero_global)
print(suma_numeros)

# """ 
# 2- Realizar una función recursiva que calcule la potencia de un número:
# """
def calcular_potencia(base:int, exponente:int) -> int:
    if exponente == 0 :
        resultado = 1
    else:
        resultado = base * calcular_potencia(base,exponente - 1)
    return resultado
base_global = 5
exponente_global = 5
resultado_potencia = calcular_potencia(base_global,exponente_global )
print(resultado_potencia)


# """3- Realizar una función recursiva que la suma de los dígitos de un número:"""
def sumar_digitos(numero: int) -> int:
    if numero < 10:
        return numero
    else:
        modulo_numero = numero % 10
        return modulo_numero + sumar_digitos(numero // 10);
   
numero = 128
print(sumar_digitos(numero))

""" 4- Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:
"""

def calcular_fibonacci(mensaje: str, minimo:int, maximo:int, reintentos: int):
    if numero < 2:
        return numero
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2);
    
numero_base = get_int("ingrese su legajo: ", 1000, 2000, 3)# 1000 - 2000mary
print(calcular_fibonacci(numero_base))

