import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Marilyn
apellido: Celis
---
Enuciado:
Al presionar el botón ‘Informar’ mostrar mediante alert los siguientes mensajes 
en función del mes seleccionado:
    Si tiene 28 días
    Si tiene 30 días
    Si tiene 31 días
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_meses = customtkinter.CTkLabel(master=self, text="Meses")
        self.label_meses.grid(row=0, column=0, padx=20, pady=10)
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        self.combobox_mes = customtkinter.CTkComboBox(master=self, values=meses)
        self.combobox_mes.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        mes_del_anio = self.combobox_mes.get();
        
        
        match(mes_del_anio):
            case "Febrero":
                mensaje = " Si tiene 28 días";
            case "abril" | "junio" | "septiembre" | "noviembre":
                mensaje = "Si tiene 30 días";
            case "enero" | "marzo" | "mayo" | "julio" | "agosto" | "octubre" | "diciembre":
                mensaje = "Si tiene 31 días";
            case _:
                 mensaje = "no hay mensajes para el mes indicado";  
        alert(None,mensaje);  
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()