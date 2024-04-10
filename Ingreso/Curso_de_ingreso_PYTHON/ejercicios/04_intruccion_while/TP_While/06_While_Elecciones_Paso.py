import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        contador = 0;
        suma_edades = 0;
        promedio_edades = 0;
        suma_votos = 0;
     
        candidato_mas_votos: 0;
        nombre_candidato_mas_votos: None;
        
        candidato_menos_votos: 0;
        
        edad_menos_votos = 0;
        
        seguir_agregando_candidatos = "si";
        while seguir_agregando_candidatos == "si":
            nombre_ingresado = prompt("nombre","ingrese nombre");
            edad_ingresada = prompt("edad","ingrese la edad");
            edad_ingresada = int(edad_ingresada);
            
            while edad_ingresada < 25:
                alert("error de edad","tiene que ser mayor a 25");
                edad_ingresada = prompt("edad","ingrese la edad");
                edad_ingresada = int(edad_ingresada);
                
            suma_edades += edad_ingresada;
            
            cantidad_votos = prompt("votos","ingrese la cantidad de votos");
            cantidad_votos = int(cantidad_votos);
            while cantidad_votos < 0:
                alert("error de votos","tiene que ser mayor de 0");
                cantidad_votos = prompt("error de votos","ingrese la cantidad de votos");
                cantidad_votos = int(cantidad_votos);  
            suma_votos += cantidad_votos;                  
                
            if contador == 0:
                candidato_mas_votos = cantidad_votos;
                nombre_candidato_mas_votos = nombre_ingresado;  
            else:
                if cantidad_votos > candidato_mas_votos:
                     candidato_mas_votos = cantidad_votos;
                     nombre_candidato_mas_votos = nombre_ingresado;
                else:
                    candidato_menos_votos = cantidad_votos
                    nombre_candidato_menos_votos = nombre_ingresado;                  
                    edad_menos_votos = edad_ingresada;
            
            seguir_agregando_candidatos = prompt("seguir agregando","quiere seguir agregando?");
            if seguir_agregando_candidatos != "si":
                break        
        
            contador += 1;
        
        promedio_edades = suma_edades / contador;
        
        print(f"nombre candidato mas votado: {nombre_candidato_mas_votos}, nombre y edad del menos votado {nombre_candidato_menos_votos} {edad_menos_votos}, promedio de edades: {promedio_edades}, total de votos: {suma_votos}")
        
                    
                         
                    
                    
                
            
                
                
            


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
