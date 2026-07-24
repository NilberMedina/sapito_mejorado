import pygame

class SapitoGrafico:
    def __init__(self, tam_celda=60, escala=0.3):  
        self.tam_celda = tam_celda
        self.escala = escala 
        self.paleta = {
            "cuerpo": (60, 179, 75),
            "sombra": (40, 140, 55),
            "brillo": (140, 220, 140),
            "ojo": (30, 70, 35),
            "ojo_brillo": (255, 255, 255),
        }
    
    def _posicion_a_pixeles(self, fila, columna):
        c = self.tam_celda
        return (columna * c + c // 2, fila * c + c // 2)
    
    def _dedo(self, lienzo, color, base, punta, grosor, radio_punta):
        pygame.draw.line(lienzo, color, base, punta, grosor)
        pygame.draw.circle(lienzo, color, punta, radio_punta, 0)
    
    def _abanico_dedos(self, lienzo, color, origen, puntas, grosor, radio):
        for punta in puntas:
            self._dedo(lienzo, color, origen, punta, grosor, radio)
    
    def _brazo(self, lienzo, color, factor, signo):
        centro_x = 3.5
        hombro = ((centro_x + signo * 0.8) * factor, 3.1 * factor)
        mano = ((centro_x + signo * 1.6) * factor, 1.85 * factor)
        
        pygame.draw.line(lienzo, color, hombro, mano, int(factor * 0.45))
        pygame.draw.circle(lienzo, color, mano, factor * 0.22, 0)
        
        puntas = [
            ((centro_x + signo * 2.0) * factor, 1.55 * factor),
            ((centro_x + signo * 1.75) * factor, 1.4 * factor),
            ((centro_x + signo * 1.45) * factor, 1.35 * factor),
            ((centro_x + signo * 1.15) * factor, 1.5 * factor),
        ]
        self._abanico_dedos(lienzo, color, mano, puntas, int(factor * 0.18), factor * 0.09)
    
    def _pierna(self, lienzo, color, factor, signo):
        centro_x = 3.5
        cadera = ((centro_x + signo * 0.8) * factor, 4.4 * factor)
        rodilla = ((centro_x + signo * 1.6) * factor, 4.9 * factor)
        pie = ((centro_x + signo * 2.0) * factor, 5.7 * factor)
        
        pygame.draw.line(lienzo, color, cadera, rodilla, int(factor * 0.5))
        pygame.draw.line(lienzo, color, rodilla, pie, int(factor * 0.5))
        pygame.draw.circle(lienzo, color, pie, factor * 0.22, 0)
        
        puntas = [
            ((centro_x + signo * 2.4) * factor, 5.9 * factor),
            ((centro_x + signo * 2.15) * factor, 6.05 * factor),
            ((centro_x + signo * 1.85) * factor, 6.1 * factor),
            ((centro_x + signo * 1.55) * factor, 5.95 * factor),
        ]
        self._abanico_dedos(lienzo, color, pie, puntas, int(factor * 0.18), factor * 0.09)
    
    def render(self, pantalla, fila, columna):
        e = self.tam_celda
        p = self.paleta
        factor = (e / 2) * self.escala  # Aplicamos la escala al factor
        
        # Obtener posición en píxeles
        x, y = self._posicion_a_pixeles(fila, columna)
        
        # Ajustamos el tamaño del lienzo según la escala
        tamanio_lienzo = int(3 * e * self.escala)
        lienzo = pygame.Surface((tamanio_lienzo, tamanio_lienzo), pygame.SRCALPHA)
        
        # Cuerpo
        cabeza = (2.4 * factor, 1.7 * factor, 2.2 * factor, 2.0 * factor)
        panza = (2.0 * factor, 3.2 * factor, 3.0 * factor, 1.8 * factor)
        
        # Sombra
        pygame.draw.ellipse(lienzo, p["sombra"], (cabeza[0], cabeza[1] + 3, cabeza[2], cabeza[3]), 0)
        pygame.draw.ellipse(lienzo, p["sombra"], (panza[0], panza[1] + 4, panza[2], panza[3]), 0)
        
        # Cuerpo principal
        pygame.draw.ellipse(lienzo, p["cuerpo"], cabeza, 0)
        pygame.draw.ellipse(lienzo, p["cuerpo"], panza, 0)
        
        # Brillo
        pygame.draw.ellipse(
            lienzo, p["brillo"],
            (cabeza[0] + cabeza[2] * 0.18, cabeza[1] + cabeza[3] * 0.08,
             cabeza[2] * 0.4, cabeza[3] * 0.25), 0
        )
        
        # Ojos
        ojo_izq = (3.0 * factor, 2.1 * factor)
        ojo_der = (4.0 * factor, 2.1 * factor)
        for ojo in (ojo_izq, ojo_der):
            pygame.draw.circle(lienzo, p["ojo"], ojo, factor * 0.32, 0)
            pygame.draw.circle(
                lienzo, p["ojo_brillo"],
                (ojo[0] - factor * 0.1, ojo[1] - factor * 0.1),
                factor * 0.08, 0
            )
        
        # Boca
        boca_rect = pygame.Rect(0, 0, factor * 0.9, factor * 0.5)
        boca_rect.center = (3.5 * factor, 2.55 * factor)
        pygame.draw.arc(lienzo, p["ojo"], boca_rect, 3.4, 6.0, max(1, int(factor * 0.06)))
        
        # Brazos
        self._brazo(lienzo, p["cuerpo"], factor, signo=-1)
        self._brazo(lienzo, p["cuerpo"], factor, signo=+1)
        
        # Piernas
        self._pierna(lienzo, p["cuerpo"], factor, signo=-1)
        self._pierna(lienzo, p["cuerpo"], factor, signo=+1)
        
        # Posicionamiento (sin rotación)
        traslacion = lienzo.get_rect(center=(x, y))
        pantalla.blit(lienzo, traslacion)
    
    def update(self):
        pass