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
Obtener el valor del mes seleccionado en el combobox_mes y  
al presionar el botón ‘Informar’ mostrar mediante alert los siguientes mensajes 
en función del mes seleccionado:
    Si el mes seleccionado es Enero: ‘que comiences bien el año!!!’
    Si el mes seleccionado es Marzo: ‘a clases!!’
    Si el mes seleccionado es Julio: ‘se vienen las vacaciones!!’
    Si el mes seleccionado es Diciembre: ‘Felices fiestas!!!’

En caso de seleccionar un mes distinto a los mencionados, no hacer nada
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label_meses = customtkinter.CTkLabel(master=self, text="Meses")
        self.label_meses.grid(row=0, column=0, padx=20, pady=10)
        meses = ["Verano","Otoño","Invierno","Primavera"]
        self.combobox_mes = customtkinter.CTkComboBox(master=self, values=meses)
        self.combobox_mes.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        
#     La empresa spaceX , nos contrata para poder hacer el cálculo de precio final y descuentos para un viaje al espacio exterior
# el costo por millón de kilómetros es de 8 bitcoin 

# podes viajar a Marte (60 millones de KM) , la Luna (½ millón de KM)y a Titan (1300 millones de KM)
# podes elegir si viajar en verano, primavera  otoño o invierno.

# para los viajes a Marte
# Si viajan más de 5 personas te hacemos un 50 % de descuento sobre el precio,
# viajando en verano al precio con descuento se le suma un 10% , en otoño y primavera se le suma un 25% al precio con descuento.

# para los viajes la Luna 
# si viajan más de 5 personas te hacemos un 40 % de descuento sobre el precio,
# viajando en verano al precio con descuento se le suma un 15% ,  en otoño y primavera al precio con descuento se le suma un 25%

# para los viajes a Titan
# si viajan más de 5 personas te hacemos un 30 % de descuento sobre el precio,
# viajando en verano al precio final se le suma un 10% , en otoño y primavera al precio con descuento se le suma un 20%

     mes_del_anio = self.combobox_mes.get();
     viajes = prompt("Destino","Ingrese un destino");
     cantidad_de_personas = prompt("personas","ingrese la cantidad de personas");
     cantidad_de_personas = int(cantidad_de_personas);
     
     kilometros_ingresado = prompt("Kilometros","ingrese los kilometros");
     kilometros_ingresado = float(kilometros_ingresado);
     precio_por_kilometros = kilometros_ingresado * 8;
        
     
     
     porcentaje_descuento = 1;
     #los mensajes de error los voy a usar con if
     mensaje_error = "Tiene que ser mas de 5 personas";  
   
     
     match(viajes):
         case "Marte":
             
             if cantidad_de_personas > 4  :
                if mes_del_anio == "Invierno" :
                    porcentaje_descuento = 50;
                elif  mes_del_anio == "Verano" : 
                     porcentaje_descuento = 60; 
                elif  mes_del_anio == "Otoño" or "Primavera" :
                    porcentaje_descuento = 75;  
                else:
                     mensaje_error ;  
                
         case "Luna":
                if cantidad_de_personas > 4  :
                    if mes_del_anio == "Invierno" :
                        porcentaje_descuento = 40;
                    elif  mes_del_anio == "Verano" : 
                        porcentaje_descuento = 55; 
                    elif  mes_del_anio == "Otoño" or "Primavera" :
                        porcentaje_descuento = 65;  
                    else:
                        mensaje_error ;  
                        
           
         case "Titan":
                if cantidad_de_personas > 4  :
                    if mes_del_anio == "Invierno" :
                        porcentaje_descuento = 30;
                    elif  mes_del_anio == "Verano" : 
                        porcentaje_descuento = 40; 
                    elif  mes_del_anio == "Otoño" or "Primavera" :
                        porcentaje_descuento = 50;  
                    else:
                        mensaje_error ;  
                        
             
         case _:
             mensaje_error_viajes = "tiene que elegir un destino valido"
         
     descuento_a_aplicar = ( precio_por_kilometros * porcentaje_descuento) / 100;
     descuento_aplicado = precio_por_kilometros - descuento_a_aplicar;
     precio_final = descuento_aplicado * cantidad_de_personas;
     
     alert("Precio final",precio_final);
     
     
     


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #  mes_del_anio = self.combobox_mes.get();
        
        
        #  match(mes_del_anio):
        #     case "Enero":
        #         mensaje = "Que comiences bien el año";
        #     case "Marzo":
        #         mensaje = "a clases!";
        #     case "Julio":    
        #          mensaje = "se vienen las vacaciones!!"; 
        #     case "Diciembre" :
        #          mensaje = "Felices fiestas!!!";  
        #     case _:
        #          mensaje = "no hay mensajes para el mes indicado";  
        #  alert(None,mensaje);  
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()