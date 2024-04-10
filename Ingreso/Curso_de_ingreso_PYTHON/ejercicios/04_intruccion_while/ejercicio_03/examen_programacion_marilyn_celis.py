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
De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el sexo mas ingresado (F o M)
Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
Informe C- El nombre de la mascota más pesada
Informe D- El sexo y nombre del gato más viejo
Informe E- El promedio de edad de todas las mascotas
Condiciones de aprobación:
Se debe realizar el ingreso de datos de manera correcta con las validaciones correspondientes siguiendo las
reglas de estilo de la cátedra y al menos uno de los informes solicitados de manera perfecta para obtener una
nota 6(seis)
Cada informe adicional logrado correctamente suma un punto más hasta obtener nota 10(diez)
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_pedir_clave = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_pedir_clave_on_click)
        self.btn_pedir_clave.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_pedir_clave_on_click(self):
        contador = 0;
        contador_masculino = 0;
        contador_femenino = 0;
        
        contador_gato = 0;
        contador_exotico = 0;
        contador_perro = 0;
        
        nombre_mascota_pesada = "todas las mascotan pesan lo mismo";
        peso_mascota_pesada = 0;
        
        nombre_gato_mas_viejo = "todos los gatos tienen la misma edad";
        edad_gato_mas_viejo = 0;
        sexo_gato_mas_viejo = None;
        
        acumulador_edad_gato = 0;
        acumulador_edad_perro = 0;
        acumulador_edad_exotico = 0;
       
        for i in range(0,5):
            nombre = prompt("nombre","ingrese el nombre de la mascota");

            peso = prompt("peso","ingrese el peso de la mascota");
            peso = int(peso);
            while peso < 10 or peso > 80:
                    alert("error","el peso tiene que estar entre 10 y 80"); 
                    peso = prompt("peso","ingrese nuevamente el peso de la mascota");
                    peso = int(peso);
            
            edad = prompt("edad","ingrese la edad");
            edad = int(edad); 
            while edad < 1:
                    alert("error","la edad tiene que ser mayor a 0");
                    edad = prompt("edad","ingrese nuevamente la edad");
                    edad = int(edad);                
                
            sexo = prompt("peso","ingrese el sexo (f o m)");  
            match sexo:
                case "m":
                    contador_masculino += 1;
                case "f":
                    contador_femenino += 1;                   
                case _:
                    alert("error","el sexo tiene que ser f o m"); 
            
            tipo_mascota = prompt("tipo mascota","ingrese el tipo de mascota");    
            match tipo_mascota:
                case "gato":
                    contador_gato += 1;
                    acumulador_edad_gato += edad;
                    if contador_gato == 1:
                        nombre_gato_mas_viejo = nombre;
                        edad_gato_mas_viejo = edad;
                        sexo_gato_mas_viejo = sexo;
                    else:
                        if edad > edad_gato_mas_viejo:
                            nombre_gato_mas_viejo = nombre;
                            edad_gato_mas_viejo = edad;
                            sexo_gato_mas_viejo = sexo;                
                case "perro":
                    contador_perro += 1;   
                    acumulador_edad_perro += edad;                
                case "exotico":
                    contador_exotico += 1;   
                    acumulador_edad_exotico += edad;                
                case _:
                    alert("error","el tipo tiene que ser gato, perro o exotico"); 
                    
            if contador == 0:
                nombre_mascota_pesada = nombre;
                peso_mascota_pesada = peso;
            else:
                if peso_mascota_pesada < peso:
                    nombre_mascota_pesada = nombre;
                    peso_mascota_pesada = peso;
                    
            contador += 1;  
        
        if contador_masculino > contador_femenino:
            sexo_mas_ingresado = "masculino";
        else:
            sexo_mas_ingresado = "femenino";
        
        suma_tipo_mascota = contador_exotico + contador_gato + contador_perro;
        porcentaje_exotico = (contador_exotico * 100 ) / suma_tipo_mascota;
        porcentaje_gato = (contador_gato * 100 ) / suma_tipo_mascota;
        porcentaje_perro = (contador_perro * 100 ) / suma_tipo_mascota;
        
        suma_edades = acumulador_edad_perro + acumulador_edad_exotico + acumulador_edad_gato;
        promedio_edad = suma_edades / contador;
        
        #Informe A- Cuál fue el sexo mas ingresado (F o M)
        print(f"el sexo mas ingresado es:{sexo_mas_ingresado}");
        
        #Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
        print(f"porcentaje de exotico:{porcentaje_exotico}%");                                    
        print(f"porcentaje de gato:{porcentaje_gato}%");                                    
        print(f"porcentaje de perro:{porcentaje_perro}%");                                    
        
        #Informe C- El nombre de la mascota más pesada
        print(f"nombre de la mascota mas pesada:{nombre_mascota_pesada}"); 
        
        #Informe D- El sexo y nombre del gato más viejo
        print(f"nombre del gato mas viejo:{nombre_gato_mas_viejo} y su sexo {sexo_gato_mas_viejo}"); 
        
        #Informe E- El promedio de edad de todas las mascotas
        print(f"promedio de edad de las mascotas: {promedio_edad}");
                             
   
                   
     

           
        
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()