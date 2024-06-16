import re
def leer_archivos(path:str, lista):
    try:
        with open(path, "r", encoding="utf-8") as archivo:
            contador_lineas = 0
            for linea in archivo:
                # print(f"Leyendo línea {contador_lineas}: {linea.strip()}")
                if contador_lineas == 0:
                    contador_lineas += 1
                    continue
                
                registro = re.split(",|\n",linea)
                diccionario = {
                    "id": registro[0],
                    "nombre": registro[1],
                    "apellido": registro[2],
                    "dni": registro[3],
                    "puesto": registro[4],
                    "sueldo": registro[5]
                }
                contador_lineas += 1
               
                lista.append(diccionario)
        return lista
               
                
    except:
        return "A ocurrido un error al generar la lista en el archivo"  
    
def guardar_empleados(path:str, lista:list):
    try:
        with open(path, "w", encoding="utf-8") as archivo:
            for empleado in lista:
                linea = f"{empleado["id"]},{empleado["nombre"]}, {empleado["apellido"]},{empleado["dni"]},{empleado["puesto"]},{empleado["sueldo"]}"
                archivo.write(linea)
                
        return lista        
    except:
        return "A ocurrido un error al generar la lista en el archivo" 
                
    
    
