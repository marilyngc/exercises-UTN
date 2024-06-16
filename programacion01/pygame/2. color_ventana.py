import pygame 

pygame.init() # inicializado pygame

ventana = pygame.display.set_mode((500, 200)) # pixeles

pygame.display.set_caption("Mi primer ventana") # titulo ed la ventana

rojo = (255,0,0)
ventana.fill(rojo) # rellenar la ventana con un color

flag = True

while flag == True: # blucle infinito
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: # pregunto si presiono la X de la ventana
            flag = False
    pygame.display.update()
pygame.quit()             
        