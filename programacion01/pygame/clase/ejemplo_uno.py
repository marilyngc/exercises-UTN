import pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)

pygame.init()

ventana = pygame.display.set_mode((500, 700)) # pixeles
pygame.display.set_caption("Mi primer ventana") # titulo ed la ventana
icono = pygame.image.load("programacion01/pygame/clase/utn_icono.jpg")
# seteo el icono
pygame.display.set_icon(icono)

## crear umagen en la superficie
gatito = pygame.image.load("programacion01/pygame/clase/gatito.jpeg")
gatito = pygame.transform.scale(gatito,(100,100)) # cambiar tamaño de la imagen

gatito_rectangulo = gatito.get_rect()# rectangulo en el gatito
gatito_rectangulo.topleft = (200,150)

# crear fuente
fuente = pygame.font.SysFont("Arial",60) # definir la configuracion de la fuente
texto = fuente.render("Miau, soy un gato",False,(0,0,0),(0,150,255))



flag = True

while flag:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if gatito_rectangulo.collidepoint(evento.pos):
                
                ventana.blit(texto,(100,150))
                
    
    ventana.blit(gatito,gatito_rectangulo)
    
    
    pygame.display.update()            


pygame.quit()            
