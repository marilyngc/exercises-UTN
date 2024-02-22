import random
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Marilyn
apellido: Celis
---
Ejercicio: for_09
---
Enunciado:
Al comenzar el juego generamos un número secreto del 1 al 100, se pedira al usuario el ingreso de un numero por prompt y si el número ingresado es el mismo que el número secreto se dará por terminado el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “Usted es un psíquico”.
	2° intento: “Excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	7 intentos: “Perdiste, suerte para la próxima”.

de no ser igual se debe informar si 
“Falta…”  para llegar al número secreto  o si 
“Se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_secreto = random.randint(0,3);
        contador_de_intentos = 0;
        
        numero_ingresado = prompt("numero secreto","ingrese un numero secreto");
        numero_ingresado = int(numero_ingresado);
        
        adivino = False;
        
        for i in range(1,3 + 1):
  
            print("numero secreto",numero_secreto)
            if numero_secreto == numero_ingresado:
                contador_de_intentos += 1;  
                adivino = True;
                
            elif numero_ingresado < numero_secreto:
                print("el numero es menor al numero secreto");
            else:
                print("el numero es mayor al numero secreto");
                    
            if adivino :
                match contador_de_intentos:
                    case 1:
                        print("1° intento: “Usted es un psíquico");        
                    case 2: 
                        print("2° intento: “Excelente percepción.")       
                    case 3: 
                        print("3° intento: “Esto es suerte”.")       
                    case 4 | 5 | 6: 
                         print("4° hasta 6° intento: “Excelente técnica")           
                    case _:
                        print("7 intentos: “Perdiste, suerte para la próxima")
            else:
                print(f"{numero_ingresado} no es el numero secreto");        
                    
               
                
                
            
        
       
                

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()