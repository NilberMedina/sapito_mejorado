import pygame

class CarroGrafico:
    
    def __init__(self, tam_celda=60):
        self.tam_celda = tam_celda
    
    def _posicion_a_pixeles(self, fila, columna):
        c = self.tam_celda
        return (columna * c + c // 2, fila * c + c // 2)
    
    def render(self, pantalla, fila, columna):
        x, y = self._posicion_a_pixeles(fila, columna)
        
        c = (220, 60, 60)
        oscuro = (40, 40, 40)
        vidrio = (120, 160, 200)
        acero = (90, 90, 90)
        
        factor = self.tam_celda / 2.5
        lienzo = pygame.Surface((3 * self.tam_celda, 3 * self.tam_celda), pygame.SRCALPHA)
        
        # Carrocería
        carroceria = [
            (1.6 * factor, 4.4 * factor),
            (1.6 * factor, 3.15 * factor),
            (1.95 * factor, 2.65 * factor),
            (2.25 * factor, 2.2 * factor),
            (3.5 * factor, 2.2 * factor),
            (3.5 * factor, 3.05 * factor),
            (3.85 * factor, 3.05 * factor),
            (5.7 * factor, 3.05 * factor),
            (5.7 * factor, 4.4 * factor),
        ]
        pygame.draw.polygon(lienzo, c, carroceria, 0)
        
        # Parachoques delantero
        pygame.draw.rect(lienzo, acero, (1.55 * factor, 4.1 * factor, 0.35 * factor, 0.3 * factor), 0)
        
        # Parrilla
        pygame.draw.rect(lienzo, acero, (1.62 * factor, 3.3 * factor, 0.25 * factor, 0.5 * factor), 0)
        
        # Parabrisas
        parabrisas = [(2.0 * factor, 3.1 * factor), (2.3 * factor, 2.35 * factor), 
                     (2.85 * factor, 2.35 * factor), (2.85 * factor, 3.1 * factor)]
        pygame.draw.polygon(lienzo, vidrio, parabrisas, 0)
        
        # Ventana lateral
        pygame.draw.rect(lienzo, vidrio, (2.95 * factor, 2.35 * factor, 0.45 * factor, 0.55 * factor), 0)
        
        # Línea de puerta
        pygame.draw.line(lienzo, oscuro, (3.35 * factor, 3.0 * factor), (3.35 * factor, 4.35 * factor), 3)
        
        # Manija
        pygame.draw.circle(lienzo, oscuro, (3.1 * factor, 3.6 * factor), factor * 0.06, 0)
        
        # Platón
        pygame.draw.rect(lienzo, oscuro, (3.8 * factor, 3.05 * factor, 0.08 * factor, 1.3 * factor), 0)
        for lx in (4.3, 4.8, 5.3):
            pygame.draw.line(lienzo, oscuro, (lx * factor, 3.15 * factor), (lx * factor, 4.35 * factor), 2)
        
        # Barandal
        pygame.draw.rect(lienzo, oscuro, (3.85 * factor, 3.0 * factor, 1.85 * factor, 0.1 * factor), 0)
        
        # Zócalo
        pygame.draw.rect(lienzo, oscuro, (1.65 * factor, 4.3 * factor, 2.1 * factor, 0.12 * factor), 0)
        
        # Ruedas
        pygame.draw.circle(lienzo, oscuro, (2.35 * factor, 4.4 * factor), factor * 0.62, 0)
        pygame.draw.circle(lienzo, c, (2.35 * factor, 4.4 * factor), factor * 0.28, 0)
        
        pygame.draw.circle(lienzo, oscuro, (5.0 * factor, 4.4 * factor), factor * 0.62, 0)
        pygame.draw.circle(lienzo, c, (5.0 * factor, 4.4 * factor), factor * 0.28, 0)
        
        traslacion = lienzo.get_rect(center=(x, y))
        pantalla.blit(lienzo, traslacion)