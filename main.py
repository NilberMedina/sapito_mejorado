# main_separado.py
import pygame
import sys
from controladores.juego_controller import JuegoController

def main():
    pygame.init()
    
    ANCHO = 720
    ALTO = 600
    
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Sapito")
    
    clock = pygame.time.Clock()
    
    # Crear el controlador
    juego = JuegoController(tam_celda=60)
    
    running = True
    
    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
            juego.manejar_evento(evento)
        
        # Actualizar lógica
        juego.update()
        
        # Dibujar
        pantalla.fill((200, 200, 200))
        juego.render(pantalla)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()