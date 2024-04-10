import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre: Marilyn
apellido: Celis
---

Enunciado:

De 5 personas que ingresan al hospital se deben tomar y validar los siguientes datos.
    ● Nombre 
    ● Temperatura, entre 35 y 42
    ● Sexo( f, m , nb )
    ● Edad(mayor a 0)

Pedir datos por Prompt y mostrar por Print

Punto A - por el número de DNI del alumno:

DNI terminados en 0 o 1

1) Informar la cantidad de personas de sexo femenino
2) La edad promedio de personas de sexo masculino
3) El nombre de la persona la persona de sexo nb con más temperatura(si la hay)

DNI terminados en 2 o 3
1) Informar la cantidad de personas de sexo masculino
2) La edad promedio de personas de sexo nb
3) El nombre de la persona de sexo femenino con la temperatura mas baja(si la hay)

DNI terminados en 4 o 5
1) Informar la cantidad de personas de sexo nb
2) La edad promedio de personas de sexo femenino
3) El nombre de la persona la persona de sexo masculino con la temperatura mas baja(si la hay)

DNI terminados en 6 o 7
1) Informar la cantidad de personas mayores de edad (desde los 18 años)
2) La edad promedio en total de todas las personas mayores de edad (18 años)
3) El nombre de la persona la persona de sexo masculino con la temperatura mas baja(si la hay)

DNI terminados en 8 o 9
1) Informar la cantidad de personas menores de edad (menos de 18 años)
2) La temperatura promedio en total de todas las personas menores de edad
3) El nombre de la persona de sexo femenino con la temperatura mas baja(si la hay)

Todos los alumnos:
B - Informar cual fue el sexo mas ingresado
C - El porcentaje de personas con fiebre y el porcentaje sin fiebre
"""
Al presionar el botón Mostrar 5 veces un mensaje (utilizando el Dialog Alert) con números DESCENDENTES, desde el 1 al 5.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador = 0;
        contador_femenino = 0;
        contador_masculino = 0;
        contador_nb = 0;
     
        
        suma_edad_masculina = 0;
        suma_edad_nb = 0;
        suma_edad_femenino = 0;
        
        promedio_edad_masculino = 0;
        promedio_edad_bn = 0;
        
        nombre_mas_temperatura_nb = 0;
        nombre_baja_temperatura_nb = 0;
        
        nombre_mas_temperatura_femenino = 0;
        nombre_baja_temperatura_femenino = 0;
        
        nombre_baja_temperatura_masculino  = 0;
        nombre_mas_temperatura_masculino = 0;
        temperatura_mas_alta_masculino = 0;
        
        persona_con_fiebre = 0;
        persona_sin_fiebre = 0;
        
        suma_con_fiebre = 0;
        suma_si_fiebre = 0;
        
        cantidad_personas_mayor= 0;
        suma_edades = 0;
        promedio_personas_mayor = 0;
        
        sexo_mas_ingresado = 0;
    
        boton_continuar = "si";
        
        
        while boton_continuar == "si":
            dni_ingresado = prompt("dni","ingrese dni");
            dni_ingresado = int(dni_ingresado);  
                     
            while dni_ingresado < 9999999:
                alert("error DNI","ingrse un dni valido");
                dni_ingresado = prompt("dni","ingrese dni");
                dni_ingresado = int(dni_ingresado);
 
            nombre_ingresado = prompt("nombre","ingrese nombre");
            
            temperatura_ingresada = prompt("temperatura","ingrese temperatura");
            temperatura_ingresada = int(temperatura_ingresada);
            while temperatura_ingresada < 35 or temperatura_ingresada > 41:
                alert("error temperatura","ingrse temperatura mayor a 35 y menos de 42");            
                temperatura_ingresada = prompt("temperatura","ingrese temperatura");
                temperatura_ingresada = int(temperatura_ingresada);
                      
            edad_ingresada = prompt("edad","ingrese la edad");
            edad_ingresada = int(edad_ingresada);                   
            while edad_ingresada < 1:
                alert("error edad","ingrese una edad mayor a 0");                
                edad_ingresada = prompt("edad","ingrese la edad");
                edad_ingresada = int(edad_ingresada);         
                       
            sexo_ingresado = prompt("sexo","sexo ingresado");
            

            match(sexo_ingresado):
                case "m":
                    contador_masculino += 1; 
                    suma_edad_masculina += edad_ingresada;  
                    if contador_masculino == 1:
                         nombre_mas_temperatura_masculino = nombre_ingresado;
                         temperatura_mas_alta_masculino = temperatura_ingresada;     
                    else:     
                        if temperatura_mas_alta_masculino < temperatura_ingresada:
                            nombre_mas_temperatura_masculino = nombre_ingresado;
                            temperatura_mas_alta_masculino = temperatura_ingresada; 
                       
                case "f":
                    contador_femenino += 1;
                    suma_edad_femenino += edad_ingresada;
                    if temperatura_ingresada > 37:
                        persona_con_fiebre += 1;
                        nombre_mas_temperatura_femenino = nombre_ingresado;
                    else:
                        persona_sin_fiebre += 1;
                        nombre_baja_temperatura_femenino = nombre_ingresado;                           
                case "nb":
                    contador_nb += 1;
                    suma_edad_nb += edad_ingresada;
                    if temperatura_ingresada > 37:
                        persona_con_fiebre += 1;
                        nombre_mas_temperatura_nb = nombre_ingresado; 
                    else:
                        persona_sin_fiebre += 1;
                        nombre_baja_temperatura_nb = nombre_ingresado;              
                case _:
                    alert("erro sexo","ingrese un sexo valido");
                    
            if temperatura_ingresada > 37:
                persona_con_fiebre += 1;
            else:
                persona_sin_fiebre += 1;
                 
                
            if edad_ingresada > 17:
                cantidad_personas_mayor += 1;
                suma_edades += edad_ingresada;
                            
            contador += 1;
            suma_con_fiebre += persona_con_fiebre;
            suma_sin_fiebre += persona_sin_fiebre;
            
            boton_continuar = prompt("continuar?","ingrese si o no");  
            if boton_continuar != "si":
                break   

        if suma_edades == 0 and cantidad_personas_mayor == 0:
            promedio_personas_mayor = 0;
        else:        
            promedio_personas_mayor  = suma_edades / cantidad_personas_mayor; 
            
        # punto B
        
        if contador_masculino > contador_femenino > contador_nb:
            sexo_mas_ingresado = "masculino";
        elif contador_nb > contador_masculino:
            sexo_mas_ingresado = "nb";    
        else:
            sexo_mas_ingresado = "femenino";    
        
        # punto C
        
        porcentaje_con_fiebre = (persona_con_fiebre * 100) % suma_con_fiebre;
        porcentaje_sin_fiebre = (persona_sin_fiebre * 100) % suma_sin_fiebre;
                
            
        print(f"personas mayores: {cantidad_personas_mayor} y el promedio de las personas mayores: {promedio_personas_mayor} y persona femenina con temperatura baja: {nombre_baja_temperatura_masculino} y el sexo mas ingresado es: {sexo_mas_ingresado} y porcentaje con fiebre: {porcentaje_con_fiebre} y porcentaje si fiebre {porcentaje_sin_fiebre}");
       
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()