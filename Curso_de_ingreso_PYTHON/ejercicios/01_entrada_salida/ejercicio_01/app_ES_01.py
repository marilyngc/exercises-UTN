import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Marilyn
apellido: Celis
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

'''

para saber el costo de un viaje necesitamos el siguiente algoritmo,
sabiendo que el precio por kilo de pasajero es 1000 pesos
Se ingresan todos los datos por PROMPT
los datos a solicitar de dos personas son,
nombre, edad y peso
se pide  armar el siguiente mensaje
"hola jose y maria , sus pesos son 80 kilos y 60 kilos respectivamente
, sumados da 140 kilos , el promedio de edad es 33 y su viaje vale 140 000 pesos  "
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        nombre_persona1 = prompt("nombre","persona 1 ingresa el nombre");
        edad_persona1 = prompt("edad","persona 1 ingresa la edad");
        edad_persona1 = int(edad_persona1);
        peso_persona1 = prompt("peso","persona 1 ingresa el peso");
        peso_persona1 = int(peso_persona1);
         
        nombre_persona2 = prompt("nombre","persona 2 ingresa el nombre");
        edad_persona2 = prompt("edad","persona 2 ingresa la edad");
        edad_persona2 = int(edad_persona2);
        peso_persona2 = prompt("peso","persona 2 ingresa el peso");
        peso_persona2 = int(peso_persona2);
        
        suma_de_kilos = peso_persona1 + peso_persona2; 
        
        promedio_edad = (edad_persona1 + edad_persona2) / 2;
        
        precio_por_kilo_persona1 = peso_persona1 * 1000;
        precio_por_kilo_persona2 = peso_persona2 * 1000;
        suma_de_precio = precio_por_kilo_persona1 + precio_por_kilo_persona2;
         
        alert("Mensaje a mostrar", f" Hola {nombre_persona1} y {nombre_persona2}, sus pesos son {peso_persona1} kilos y {peso_persona2} kilos respectivamente, sumados da {suma_de_kilos} kilos, el promedio de edad es de {promedio_edad} y su viaje vale {suma_de_precio} pesos");


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
