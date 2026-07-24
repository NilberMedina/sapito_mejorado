import pygame

class MapaGrafico:
    def __init__(self, tam_celda=60):
        self.tam_celda = tam_celda
    
    def _color_celda(self, simbolo):
        colores = {
            'M': (180, 220, 255), 
            'P': (90, 90, 90),     
            'V': (140, 200, 140), 
            'A': (40, 120, 40),    
        }
        return colores.get(simbolo, (200, 200, 200))
    
    def render(self, pantalla, mapa):
        c = self.tam_celda
        for f, fila in enumerate(mapa):
            for col, simbolo in enumerate(fila):
                rect = pygame.Rect(col * c, f * c, c, c)
                pygame.draw.rect(pantalla, self._color_celda(simbolo), rect)
                pygame.draw.rect(pantalla, (0, 0, 0), rect, 1)