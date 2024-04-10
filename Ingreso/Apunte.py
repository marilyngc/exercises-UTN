import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

"""
Calcular porcentaje
"""
# Definimos los valores
valor = 5  # Ejemplo de valor valor que deseas expresar como un porcentaje del total 
total = 20  # Ejemplo de total

# Calculamos el porcentaje
porcentaje = (valor / total) * 100

# Mostramos el resultado
print(f"El porcentaje es: {porcentaje}%")




"""
Calcular promedio
"""

# Definimos las variables
suma_valores = 0
cantidad_valores = 0

# Vamos ingresando valores hasta que se ingrese -1 para terminar
valor = int(input("Ingrese un valor (-1 para terminar): "))

while valor != -1:
    suma_valores += valor
    cantidad_valores += 1
    valor = int(input("Ingrese un valor (-1 para terminar): "))

# Verificamos que haya al menos un valor para evitar división por cero
if cantidad_valores > 0:
    promedio = suma_valores / cantidad_valores
    print(f"El promedio es: {promedio}")
else:
    print("No se ingresaron valores.")
    
    
    
    
"""
Pedir valores validos
"""

# forma 1
edad = 0
edad_valida = False

while not edad_valida:
    edad = int(input("Ingresa una edad: "))
    if edad >= 0:
        edad_valida = True
    else:
        print("Edad invalida")
        

# forma 2
valor = prompt("Ingresa un valor: ", "")
valor = int(valor)

while valor < 0:
    valor = prompt("Ingresa un valor: ", "")
    valor = int(valor)



"""
Calcular valor minimo y maximo 
"""

# Forma 1
valor_minimo = 0
valor_maximo = 0

for i in range(5):
    valor = int(input("Ingresa un valor: "))
    if i == 0:
        valor_minimo = valor
        valor_maximo = valor
    else:
        if valor < valor_minimo:
            valor_minimo = valor
        if valor > valor_maximo:
            valor_maximo = valor

print(f"El valor minimo es: {valor_minimo}")
print(f"El valor maximo es: {valor_maximo}")



# Forma 2 con none
valor_maximo = None
valor_minimo = None

for i in range(5):
    valor = int(input("Ingresa un valor: "))
    
    if valor_maximo == None or valor > valor_maximo:
        valor_maximo = valor
    elif valor_minimo == None or valor < valor_minimo:
        valor_minimo = valor

print(f"El valor minimo es: {valor_minimo}")
print(f"El valor maximo es: {valor_maximo}")