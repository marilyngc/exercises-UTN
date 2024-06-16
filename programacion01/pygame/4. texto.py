import pygame 

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
texto = fuente.render("HoLA PRIMERO",False,(0,0,0),(0,150,255))

flag = True

while flag == True: # blucle infinito
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: # pregunto si presiono la X de la ventana
            flag = False
    ventana.blit(texto,(50,50))    # mostrar texto y posicion (x,y)    
    pygame.display.update()
    
pygame.quit()             
        