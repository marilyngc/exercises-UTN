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

'''

""" 
Simulacro 01 - Dr. UTN


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
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador = 0;
        contador_adultos = 0;
        contador_masculino = 0;
        contador_femenino = 0;
        contador_nb = 0;
        suma_edad_adultos = 0;
        
        temperatura_mas_alta_masculino = 0;
        nombre_mas_temperatura_masculino = 0;
        personas_con_fiebre = 0;
        personas_sin_fiebre = 0;
        
        sexo_mas_ingresado = 0;
        
 
        for i in range(0,5):
            nombre = prompt("nombre","ingrese nombre");
            edad = prompt("edad","ingrese edad");    
            edad = int(edad);
            
            while edad < 1 :
                alert("error","la edad tiene que ser mayor a 0");   
                edad = prompt("edad","ingrese edad");    
                edad = int(edad); 
                
            temperatura = prompt("temperatura","ingrese temperatura"); 
            temperatura = int(temperatura);    
            while temperatura < 36 or temperatura > 39:
                alert("error","su temperatura no es valida  ");   
                temperatura = prompt("temperatura","ingrese temperatura"); 
                temperatura = int(temperatura);       
                    
            # 1) Informar la cantidad de personas mayores de edad (desde los 18 años)

            if edad > 17:
                contador_adultos += 1;
                suma_edad_adultos += edad;  
                
            #3) El nombre de la persona la persona de sexo masculino con la temperatura mas baja(si la hay)
            sexo = prompt("sexo","ingrese sexo");           
            match sexo:
                case "m":
                    contador_masculino += 1;
                    if i == 0:
                        nombre_mas_temperatura_masculino = nombre;
                        temperatura_mas_alta_masculino = temperatura;
                    else:
                        if temperatura_mas_alta_masculino < temperatura:
                            nombre_mas_temperatura_masculino = nombre;
                            temperatura_mas_alta_masculino = temperatura;

                case "f":
                    contador_femenino += 1;
                case"nb":
                    contador_nb += 1;
                case _:
                    alert("error","tiene que ingresar un sexo valido (m-f-nb)");    
            
            if temperatura > 36:
                personas_con_fiebre += 1;
            else:
                personas_sin_fiebre  += 1;   
            
            contador += 1;    
                
         #2) La edad promedio en total de todas las personas mayores de edad (18 años)               
        if suma_edad_adultos == 0 and contador == 0:
            promedio_mayores = 0;
        else:    
            promedio_mayores = suma_edad_adultos / contador_adultos;   
        
        print(contador_masculino)    
        #       B - Informar cual fue el sexo mas ingresado
        if contador_masculino > contador_femenino and contador_masculino > contador_nb:
            sexo_mas_ingresado = "masculino";
        elif contador_nb > contador_masculino and contador_nb > contador_femenino:
            sexo_mas_ingresado = "no binario";
        else:
            sexo_mas_ingresado = "femenino";
            
        # C - El porcentaje de personas con fiebre y el porcentaje sin fiebre           
        suma_temperaturas = personas_con_fiebre + personas_sin_fiebre;
        porcentaje_con_fiebre = (personas_con_fiebre * 100) / suma_temperaturas;                
        porcentaje_sin_fiebre = (personas_sin_fiebre * 100) / suma_temperaturas;                
        
     
        print(f"cantidad de personas mayores: {contador_adultos}");
        print(f"promedio de personas mayores: {promedio_mayores}");
        print(f"El nombre de la persona la persona de sexo masculino con la temperatura mas baja: {nombre_mas_temperatura_masculino}");
        print(f"el sexo mas ingresado: {sexo_mas_ingresado}");
        print(f"porcentaje de personas CON fiebre: {porcentaje_con_fiebre}");
        print(f"porcentaje de personas SIN fiebre: {porcentaje_sin_fiebre}");
   
 


 
            
        
        
        
        # for contador in range(6):
        #     alert("resultado",contador)
       
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()