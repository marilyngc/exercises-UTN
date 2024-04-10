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
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador = 0;
        cancelar = False;
        suma_positivos = 0;
        suma_negativos = 0;
       
        
        while cancelar is not None:
            numero_ingresado = prompt("numero ingresado","ingrese un numero");
            
            if numero_ingresado == None:
                break
            
            numero_ingresado = int(numero_ingresado);
            contador += 1;
        
            if numero_ingresado > 0:
                suma_positivos += numero_ingresado;
        
            else:
                suma_negativos *= numero_ingresado; 
            
           
        self.txt_suma_acumulada.delete(0,"end");    
        self.txt_suma_acumulada.insert(0,suma);   
        
        self.txt_producto.delete(0,"end");    
        self.txt_producto.insert(0,multiplicacion);    
                   
            


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
