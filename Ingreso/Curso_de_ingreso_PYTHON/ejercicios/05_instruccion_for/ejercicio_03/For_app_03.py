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
Al presionar el botón Mostrar tomar del campo de texto cantidad de veces que se desea
repetir el mensaje "Hola UTN FRA" (utilizando el Dialog Alert)



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

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_repetir = customtkinter.CTkEntry(master=self)
        self.txt_repetir.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        boton_continuar = "si";
        precio_plato = 3000;
        precio_bebida = 1000;
        
        cantidad_pizza = 0;
        cantidad_hamburguesa  = 0;
        cantidad_ensalada = 0;
        
        cantidad_refresco = 0;
        cantidad_agua = 0;
        cantidad_jugo = 0;
        
        contador_amigos = 0;
        
        suma_precio_pizza = 0;
        nombre_menor_cantidad_hamburguesa = "nadie pidio hamburguesa";
        menor_cantidad_hamburguesa = 0;
        
        contador_personas_mas_una_bebida = 0;
        contador_personas_menos_un_plato = "no hay";
        nombre_persona_con_mas_bebidas = "todos pidieron la misma cantidad";
        
        nombre_mayor_cantidad_pizza = "Nadie pidió pizza";
        mayor_cantidad_pizza = 0;
        
        precio_por_plato_refresco = 0;
        precio_por_plato_agua = 0;
        precio_por_plato_jugo = 0;
 
        
        while boton_continuar == "si":
            nombre = prompt("nombre","ingrese nombre");
            
            plato_principal = prompt("plato","ingrese plato (pizza,hamburguesa o ensalada)");
            cantidad_platos = prompt("cantidad de pizza","ingrese la cantidad");
            cantidad_platos = int(cantidad_platos);
            while cantidad_platos < 1:
                alert("error","tiene que ser minimo un plato");
                plato_principal = prompt("plato","ingrese plato (pizza,hamburguesa o ensalada)");
                
            match plato_principal:
                case "pizza":
                    cantidad_pizza += cantidad_platos;
                    suma_precio_pizza = cantidad_pizza * precio_plato;
                    
                    if contador_amigos == 0:
                        nombre_mayor_cantidad_pizza = nombre;
                        mayor_cantidad_pizza = cantidad_platos;
                    else:
                        if mayor_cantidad_pizza < cantidad_platos:
                            nombre_mayor_cantidad_pizza = nombre;
                            mayor_cantidad_pizza = cantidad_platos;                            
                case "hamburguesa":
                    cantidad_hamburguesa += cantidad_platos;
                    if contador_amigos == 0:
                        nombre_menor_cantidad_hamburguesa = nombre;
                        menor_cantidad_hamburguesa = cantidad_platos;
                    else:
                        if menor_cantidad_hamburguesa > cantidad_platos:
                            nombre_menor_cantidad_hamburguesa = nombre;
                            menor_cantidad_hamburguesa = cantidad_platos;
                                                     
                case "ensalada":
                    cantidad_ensalada += cantidad_platos;
                case _:
                    alert("error","tiene que ser pizza,hamburguesa o ensalada");
                            
            bebida_principal = prompt("bebida","ingrese bebida (refresco,agua,jugo)");
            cantidad_bebidas = prompt("cantidad bebidas","ingrese la cantidad de bebidas");
            cantidad_bebidas = int(cantidad_bebidas)  
            while cantidad_bebidas < 1:
                alert("error","tiene que ser minimo una bebida");
                bebida_principal = prompt("bebida","ingrese bebida (refresco,agua,jugo)"); 
            
            match bebida_principal:
                case "refresco":
                    cantidad_refresco += cantidad_bebidas;
                    precio_por_plato_refresco = cantidad_refresco * precio_bebida;
                case "agua":
                    cantidad_agua += cantidad_bebidas;
                    precio_por_plato_agua = cantidad_agua * precio_bebida;
                case "jugo":
                    cantidad_jugo += cantidad_bebidas;
                    precio_por_plato_jugo = cantidad_jugo * precio_bebida;
                case _:
                    alert("error","tiene que ser refresco,agua o jugo"); 
            
            if cantidad_bebidas > 1:
                contador_personas_mas_una_bebida += 1;
                if contador_personas_mas_una_bebida == 1:
                    nombre_persona_con_mas_bebidas = nombre;
                    cantidad_persona_con_mas_bebidas = cantidad_bebidas;
                else:
                    if cantidad_persona_con_mas_bebidas < cantidad_bebidas:
                        nombre_persona_con_mas_bebidas = nombre;
                        cantidad_persona_con_mas_bebidas = cantidad_bebidas;  
            
            if contador_amigos == 0:
                nombre_persona_pidio_menos_platos = nombre;
                cantidad_menos_platos = cantidad_platos;
            else:
                if cantidad_menos_platos > cantidad_platos:
                    nombre_persona_pidio_menos_platos = nombre;
                    cantidad_menos_platos = cantidad_platos;                    
                
                
                                                  
            contador_amigos += 1;
            boton_continuar = prompt("desea seguir?", "ingrese si o no");
            if boton_continuar != "si":
                break;        
            
        if cantidad_refresco > cantidad_agua and cantidad_refresco > cantidad_jugo:
            bebida_mas_elegida = "Refresco";
        elif cantidad_jugo > cantidad_refresco and cantidad_jugo > cantidad_agua:
            bebida_mas_elegida = "Jugo";
        else:
            bebida_mas_elegida = "Agua";  
        
        suma_platos = cantidad_hamburguesa + cantidad_ensalada + cantidad_pizza;
        porcentaje_hamburguesa = (cantidad_hamburguesa * 100) / suma_platos;                                 
        porcentaje_ensalada = (cantidad_ensalada * 100) / suma_platos;                                 
        porcentaje_pizza = (cantidad_pizza * 100) / suma_platos;  
                                       
        promedio_gastos_pizzas = suma_precio_pizza / contador_amigos; 
        
        suma_bebidas = cantidad_agua + cantidad_jugo + cantidad_refresco;
        promedio_bebidas =  suma_bebidas / contador_amigos;  
        
        suma_precio_bebidas = precio_por_plato_agua + precio_por_plato_jugo + precio_por_plato_refresco;
        promedio_precio_bebidas = suma_precio_bebidas / contador_amigos;   
        
        print(f"bebida mas vendida {bebida_mas_elegida}");                        
        print(f"porcentaje de hamburguesa: {porcentaje_hamburguesa}");                        
        print(f"porcentaje de ensalada: {porcentaje_ensalada}");                        
        print(f"porcentaje de pizza: {porcentaje_pizza}");                        
        print(f"total de refresco: {cantidad_refresco}");                        
        print(f"promedio gastado en pizzas: {promedio_gastos_pizzas}");                        
        print(f"nombre del que pidió menos hamburguesas: {nombre_menor_cantidad_hamburguesa}");  
        
        # BIS                      
        print(f"cantidad de personas que pidieron mas de una bebida: {contador_personas_mas_una_bebida}");                        
        print(f"cantidad de personas que pidieron menos de un plato: {contador_personas_menos_un_plato }"); 
        print(f"nombre de quien pidio mas bebidas: {nombre_persona_con_mas_bebidas}"); 
        print(f"nombre de quien pidio menos platos: {nombre_persona_pidio_menos_platos}"); 
        print(f"el nombre de la persona que pidio mas pizzas: {nombre_mayor_cantidad_pizza}"); 
        print(f"el promedio de bebidas por persona: {promedio_bebidas}"); 
        print(f"el precio promedio de bebidas pagada por cada persona: {promedio_precio_bebidas}"); 
                               
                     
            
                
            
                 
            
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()