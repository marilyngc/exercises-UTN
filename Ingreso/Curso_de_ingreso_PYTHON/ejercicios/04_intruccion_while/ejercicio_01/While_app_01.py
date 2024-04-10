import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Marilyn
apellido: Celis
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        
        "ingresamos de los  5 alumnos NOMBRE,EDAD,SEXO y altura (50 y 220) y nota (1 y 10)"
        "a- la persona mas alta b- la peor nota c- la cantidad de aprobados d-suma de las edades e-promedio de notas f- la mas vieja de las mujeres h- cantidad de aprobados por sexo"
        
        contador = 0;
        contador_aprobado = 0; 
        suma_edades = 0;
        suma_notas = 0;
        bandera_primer_mujer = 0;
        contador_mujeres_aprobadas = 0;
        contador_hombres_aprobados = 0;  
        desea_seguir = "S"
        
        while desea_seguir == "S":
            nombre = prompt("ingreso","ingrese su nombre");
            
            edad = prompt("ingreso","ingrese su edad");
            edad = int(edad);
            while edad < 18 or edad > 120:
                edad = prompt("error","reingrese su edad");
                edad = int(edad);
                
            altura = prompt("ingreso","ingrese su altura");
            altura = int(altura);  
            while altura < 50 or altura > 220:
                altura = prompt("error","reingrese su altura");
                altura = int(altura);
                
            nota = prompt("ingreso","ingrese su nota");
            nota = int(nota);  
            while nota < 1 or nota > 10:
                nota = prompt("error","reingrese su altura");
                nota = int(nota);
                
            sexo = prompt("ingreso","ingrese su sexo");
            while sexo != "f" or sexo != "m":
                sexo = prompt("error","reingrese su sexo");
                
            if contador == 0:
                mayor_altura = altura;
                nombre_mayor_altura = nombre;
                
                peor_nota = nota;
                nombre_peor_nota = nombre;
            else :
                if mayor_altura < altura:
                    mayor_altura = altura;
                    nombre_mayor_altura = nombre;
                    
                if peor_nota > nota :    
                    peor_nota = nota;
                    nombre_peor_nota = nombre;
                    
                    
            
            if nota > 5 :
                contador_aprobado += 1;  
                
                match(sexo):
                    case "f":
                        contador_mujeres_aprobadas += 1;
                    case "m":  
                        contador_hombres_aprobados += 1;  
                
                
            if sexo == "f":
                if bandera_primer_mujer == 0:
                    bandera_primer_mujer = 1;
                    edad_mas_vieja = edad;
                    nombre_mas_vieja = nombre;
                else:
                    if edad > edad_mas_vieja:
                        edad_mas_vieja = edad;
                        nombre_mas_vieja = nombre;    
                
            
            suma_edades += edad;    
            suma_notas += nota;   
            
            
            
            contador += 1;   
            desea_seguir = prompt("continuar?","ingrese s");
            
            if desea_seguir != "S":
                break   
       
                        
                    
                                    
                
        promedio_notas = suma_notas / contador;  
        
        if contador_hombres_aprobados > contador_mujeres_aprobadas:
            sexo_mas_aprobado = "hombre";        
        else:
           sexo_mas_aprobado = "mujer";      
                
            
            
       
        # contador = 0;
        # while contador < 10:
        #     contador += 1;
        #     print(contador);
        
          
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()