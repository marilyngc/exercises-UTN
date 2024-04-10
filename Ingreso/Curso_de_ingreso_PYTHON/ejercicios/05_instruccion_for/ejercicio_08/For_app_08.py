import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Marilyn
apellido: Celis
---
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_ingresado = prompt("numero","ingrese un numero");
        numero_ingresado = int(numero_ingresado);
        numeros_primos = 0;
        
        for i in range(2,numero_ingresado + 1):
            
            if numero_ingresado % i != 0  :
                break
            
            print("divisores encontrados",i);
            numeros_primos += 1 
                    
        if numero_ingresado == i:
            print("primos encontrados",i);
                        
        else:
            print("valor ingresado",f"No primos encontrados: {i}");    
        
            
                        
                    
                
       
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()