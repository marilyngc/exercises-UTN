nombres = ["GIO","MATI","GERMAN"]
apellidos = ["Lopez","Gomez","Ruiz"]
edades = [20,35,42]


with open("agendas.csv","w") as archivo:
    for i in range(len(nombres)):
        linea = f"{nombres[i]},{apellidos[i]},{edades[i]}\n"
        archivo.write(linea)
        
########### lectura ##########
import re

with open("agendas.csv","r") as archivo:
    for linea in archivo:
        # registro = linea.split(",")
        registro = re.split(", | \n", linea)
        print(linea)        
        
        