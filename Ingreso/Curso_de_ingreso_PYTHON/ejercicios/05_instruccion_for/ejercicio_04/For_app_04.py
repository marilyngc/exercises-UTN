import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Marilyn
apellido: Celis
---
Al presionar el botón Mostrar pedir valores por prompt hasta que el usuario ingrese el valor 9 (se deberá utilizar 'BREAK').

---

En el parque de diversiones "Aventuras Extremas", un grupo de 10 amigos ha 
decidido disfrutar del día probando las diferentes atracciones y luego se reúnen en un
restaurante para compartir un delicioso almuerzo. Antes de que llegue la cuenta, deciden 
crear un programa para calcular y dividir los gastos de manera equitativa. 
Se pide ingresar los siguientes datos hasta que el usuario lo desee:

Para cada amigo (pedir por prompt)

Nombre del amigo, 
Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").
Cantidad de platos principales pedidos (debe ser al menos 1).
Bebida elegida ("Refresco", "Agua", "Jugo").
Cantidad de bebidas pedidas (debe ser al menos 1).


Se conocen los siguientes precios base:

El precio unitario de cada plato principal es de $3000.

El precio unitario de cada bebida es de $1000.


Una vez ingresados todos los datos, el programa debe calcular e informar lo siguiente (informar por print):

Informar cual fue el tipo de bebida más vendida.
Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad). Ejemplo: [30% pizza, 40% ensaladas,
30% hamburguesas]
Informar la cantidad total de bebidas que fueron “Refresco”.
El promedio gastado en platos principales de tipo “Pizza” sobre el grupo de amigos en general.
El nombre de la persona que pidió la menor cantidad de platos principales de tipo “Hamburguesa”


bis 
cantidad de usuarios que pidieron mas de una bebida
cantidad de amigos que pidieron menos de un plato principal

el nombre del que compro mas bebidas
el nombre del que menos platos principales pidio 

el nombre de la persona que pidio mas pizzas
el promedio de bebidas por persona
el precio promedio de bebidas pagada por cada persona

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        boton_continuar = "si";
        
        contador_amigos = 0;
        precio_plato = 3000;
        precio_bebida = 1000;
        
        cantidad_refresco = 0;
        cantidad_agua = 0;
        cantidad_jugo = 0;
        
        cantidad_pizza = 0;
        cantidad_hamburguesa = 0;
        cantidad_ensalada = 0;
        
        suma_precios_pizza = 0;
        
        nombre_menor_hamburguesa = "No hay persona con menor hamburguesa";
        menor_cantidad_hamburguesa = 0;        
        
        while boton_continuar == "si":
            nombre = prompt("nombre","ingrese nombre");
            
            plato_principal = prompt("plato","ingrese plato (pizza,hamburguesa o ensalada)");
            cantidad_platos = prompt("cantidad de pizza","ingrese la cantidad");
            cantidad_platos = int(cantidad_platos);
            
            while cantidad_platos < 1:
                alert("error","tiene que elegir al menos un plato");
                cantidad_platos = prompt("cantidad de pizza","ingrese la cantidad");
                cantidad_platos = int(cantidad_platos);
            
            bebida_principal = prompt("bebida","ingrese bebida (refresco,agua,jugo)");
            cantidad_bebidas = prompt("cantidad bebidas","ingrese la cantidad de bebidas");
            cantidad_bebidas = int(cantidad_bebidas);
            
            while cantidad_bebidas < 1:
                alert("error","tiene que elegir al menos una bebida");                
                cantidad_bebidas = prompt("cantidad bebidas","ingrese la cantidad de bebidas");
                cantidad_bebidas = int(cantidad_bebidas);
            
            match plato_principal:
                case "pizza":
                    cantidad_pizza += cantidad_platos;
                    suma_precios_pizza += precio_plato;
                case "hamburguesa":
                    cantidad_hamburguesa += cantidad_platos;   
                    if contador_amigos == 0:
                        nombre_menor_hamburguesa = nombre;
                        menor_cantidad_hamburguesa = cantidad_platos;
                    else:
                        if cantidad_platos < menor_cantidad_hamburguesa:
                            nombre_menor_hamburguesa = nombre;
                            menor_cantidad_hamburguesa = cantidad_platos;   
                                                                          
                case "ensalada":
                    cantidad_ensalada += cantidad_platos;                    
                case _:
                     alert("error","tiene que ser pizza,hamburguesa o ensalada");                           
                            
            
            match bebida_principal:
                case "refresco":
                    cantidad_refresco += cantidad_bebidas;
                case "agua":
                    cantidad_agua += cantidad_bebidas;
                case "jugo":
                    cantidad_jugo += cantidad_bebidas;
                case _:
                     alert("error","tiene que ser refresco,jugo o agua");
                     
            contador_amigos += 1;
            
            boton_continuar = prompt("desea continuar?","ingrese si o no");
            if boton_continuar != "si":
                break      
        
        if cantidad_refresco > cantidad_agua and cantidad_refresco > cantidad_jugo:
            bebida_mas_vendida = "refresco";
        elif cantidad_jugo > cantidad_agua and cantidad_jugo > cantidad_refresco:
            bebida_mas_vendida = "jugo";                                                      
        else:
            bebida_mas_vendida = "agua";
            
        suma_cantidad_platos = cantidad_pizza + cantidad_ensalada + cantidad_hamburguesa;
        porcentaje_pizza = (cantidad_pizza * 100 ) / suma_cantidad_platos;
        porcentaje_ensalada = (cantidad_ensalada* 100 ) / suma_cantidad_platos;
        porcentaje_hamburguesa = (cantidad_hamburguesa * 100 ) / suma_cantidad_platos;
        
        promedio_pizza_gastado = suma_precios_pizza / contador_amigos;
            
        print(f"jugo mas vendido: {bebida_mas_vendida}");       
                         
        print(f"porcentaje de pizza: {porcentaje_pizza}");                        
        print(f"porcentaje de ensalada: {porcentaje_ensalada}");                        
        print(f"porcentaje de hamburguesa: {porcentaje_hamburguesa}");  
                              
        print(f"cantidad total de refresco: {cantidad_refresco}");   
                             
        print(f"promedio de pizza gastado: {promedio_pizza_gastado}");                        
        print(f"nombre de la perosna que pidió menos hamburguesa: {nombre_menor_hamburguesa}");                        
                     
            
            
        
        
        
        # for i in range(9999):
        #     valor_ingresado = prompt("valor","ingrese valor");
        #     valor_ingresado = int(valor_ingresado);
            
        #     if valor_ingresado == 9:
        #         break
        #     else:
        #         alert("valor ingresado",f"valor ingresdo es: {valor_ingresado}");
            
                
            
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()