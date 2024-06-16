import pygame

lista_nombres = ["Maria","gio","marilyn"]

pygame.init() # inicializado pygame

ventana = pygame.display.set_mode((500, 200)) # pixeles

pygame.display.set_caption("Mi primer ventana") # titulo ed la ventana

rojo = (255,0,0)
ventana.fill(rojo) # rellenar la ventana con un color

# traigo la imagen
icono = pygame.image.load("programacion01\pygame\icono.jpg")
# seteo el icono
pygame.display.set_icon(icono)


# crear fuente
fuente = pygame.font.SysFont("Arial",60) # definir la configuracion de la fuente

flag = True


while flag == True: # blucle infinito
    y = 50
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: # pregunto si presiono la X de la ventana
            flag = False
    
    for nombre in lista_nombres:
        texto = fuente.render(nombre,False,(0,0,0),(0,150,255))
        ventana.blit(texto,(50,y))    # mostrar texto y posicion (x,y)    
        y += 30
                
    pygame.display.update()
    
pygame.quit()             
        