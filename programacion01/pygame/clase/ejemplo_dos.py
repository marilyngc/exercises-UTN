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

# crear fuente
fuente = pygame.font.SysFont("Arial",20) # definir la configuracion de la fuente

# cuadro texto
input_box = pygame.Rect(50,50,200,32)
color_inactivo = AZUL
color_activo = ROJO
color_actual = color_inactivo
activo = False
texto = ""


flag = True

while flag:
    
    ## manejador de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(evento.pos):
                activo = not activo
            if activo:
                color_actual = color_activo
            else:
                color_actual = color_inactivo
        elif evento.type == pygame.KEYDOWN:
            if activo:
                if evento.key == pygame.K_BACKSPACE:
                        texto = texto[:-1]
                elif evento.key == pygame.K_ESCAPE:
                    texto = ""        
                else:        
                    texto += evento.unicode
                
    text_superface = fuente.render(texto,True, color_actual) 
    ventana.blit(text_superface,(input_box.x + 5, input_box.y + 5))
                        
    pygame.draw.rect(ventana, color_actual, input_box, 2)
    
    pygame.display.update()            


pygame.quit()            
