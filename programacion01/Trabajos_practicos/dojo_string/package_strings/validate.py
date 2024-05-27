from class_video import *


def bubble_sort(videos:list) -> list:
    for i in range(0,len(videos) - 1):
        for j in range(i + 1, len(videos)):
            if videos[i].sesion > videos[j].sesion:
                auxiliar = videos[i]
                videos[i] = videos[j]
                videos[j] = auxiliar
           
      
def promedio_vistas(video:list) -> int:
    acumulador_vistas = 0
    contador_vistas = 0
    
    for i in range(len(video)):
        acumulador_vistas += video[i].vistas
        contador_vistas += 1
        
    promedio_vistas = acumulador_vistas / contador_vistas
    promedio_vistas = promedio_vistas / 1000
    promedio_vistas = round(promedio_vistas)
    
    return promedio_vistas

def maxima_reproduccion(video:list) -> list:
    maxima_vista = 0
    array_mayor_vistas = []
    for i in range(len(video)):
        if video[i].vistas > maxima_vista:
            maxima_vista = video[i].vistas
            array_mayor_vistas.append(i)
        elif video[i].vistas >= maxima_vista:
            array_mayor_vistas.append(i)
    
    return array_mayor_vistas        
                
def busqueda_por_codigo(video:list,codigo="nick"):
    codigo_encontrado = []
    for i in range(len(video)):
        if video[i].codigo_url.count(codigo) > 0:
            codigo_encontrado.append(i)
    return codigo_encontrado        

def listado_por_colaborador(video:list,colaborador:str):
    videos_colaborador = []
    for i in range(len(video)):
        if video[i].colaborador == colaborador:
            videos_colaborador.append(i)   
    
    return videos_colaborador     

def listado_por_mes(video:list,mes:int)-> list:
    videos_mes_ingresado = []
    for i in range(len(video)):
        fecha = video[i].fecha_lanzamiento 
        if fecha.month == mes:
            videos_mes_ingresado.append(i)
    return videos_mes_ingresado                   
                    
    
    
        
        
        
    
     
    