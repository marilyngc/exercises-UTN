import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Marilyn
apellido: Celis
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        contador = 0;
        contador_bn = 0;
        contador_m = 0;
        contador_f = 0;
        nombre_menor_jr = 0;
        suma_edades_m = 0;
        suma_edades_f = 0;
        suma_edades_bn = 0;
        promedio_edades_m = 0;
        promedio_edades_f = 0;
        promedio_edades_bn = 0;
        tecnologia_python = 0;
        tecnologia_js = 0;
        tecnologia_asp= 0;
        tecnologia_mayor_postulante = 0;
        
        
        for i in range(1,2 + 1):
            nombre = prompt("nombre","ingrese nombre");         
            genero = prompt("genero","ingrese genero");
            
            if genero == "NB":
                edad = prompt("edad","ingrese edad");
                edad = int(edad);  
                if edad > 24 and edad < 41:
                    tecnologia = prompt("tecnologia","ingrese tecnologia");
                elif tecnologia ==  "ASP.NET" or "JS":
                    puesto = prompt("puesto","ingrese puesto");
                elif puesto ==  "Ssr":
                       contador_bn += 1;
                       
            edad = prompt("edad","ingrese edad");
            edad = int(edad);            
            if edad < 19:
                puesto = prompt("puesto","ingrese puesto");
                if puesto == "jr":
                    nombre_menor_jr = nombre;
            
            match genero:
                case "M":    
                     suma_edades_m += edad;
                     contador_m += 1;
                     
                case "F":  
                    suma_edades_f += edad;   
                    contador_f += 1;
                case "NB":
                    suma_edades_bn += edad;  
                    contador_bn += 1;  
                case _:
                    alert("error","ingrese un genero valido");  
                      
            tecnologia = prompt("tecnologia","ingrese tecnologia"); 
            
            match tecnologia:
                case "PYTHON":
                    tecnologia_python += 1;
                case "JS":
                    tecnologia_js += 1;
                case "ASP.NET":
                    tecnologia_asp += 1;
                case _:
                    alert("error","ingrese una tecnologia valida"); 
            
            if tecnologia_python > tecnologia_js and tecnologia_python > tecnologia_asp:
                tecnologia_mayor_postulante = "Python";
            elif tecnologia_js > tecnologia_python :
                tecnologia_mayor_postulante = "Js";
            else:
                tecnologia_mayor_postulante = "ASP.NET"       
                
                             
        
            
               
        contador += 1;
        
        # para corregir el error del divisor en cero
        if contador_m != 0:
            promedio_edades_m = suma_edades_m / contador_m;
        else:
            promedio_edades_m = 0;
            
        if contador_f != 0:
            promedio_edades_f = suma_edades_f / contador_f;
        else:
            promedio_edades_f = 0;
            
        if contador_bn != 0:
            promedio_edades_bn = suma_edades_bn / contador_bn;
        else:
            promedio_edades_bn = 0;
        
        suma_genero = contador_m + contador_f + contador_bn;
        suma_genero = float(suma_genero);
        
        porcentaje_m = (contador_m * 100  ) / suma_genero;
        porcentaje_m = float(porcentaje_m)
        
        porcentaje_f = (contador_f * 100  ) / suma_genero;
        porcentaje_f = float(porcentaje_f)
        
        porcentaje_bn = (contador_bn * 100  ) / suma_genero;
        porcentaje_bn = float(porcentaje_bn)
        
           
        print(f"cantidad de postulantes NO BINARIOS: {contador_bn} /n" 
              f"nombre del JR: {nombre_menor_jr} /n " 
              f"promedio de edad de M: {promedio_edades_m} /n "
              f"promedio de edad de F: {promedio_edades_f} /n "
              f"promedio de edad de NB: {promedio_edades_bn} /n " 
              f"tecnologia con mas postulantes: {tecnologia_mayor_postulante} /n "
              f"porcentaje de edad de M: {porcentaje_m} /n "
              f"porcentaje de edad de F: {porcentaje_f} /n "
              f"porcentaje de edad de NB: {porcentaje_bn} /n ");        
                    
                    

                    
                
            
                
                

        
                
                    
                
                
                


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
