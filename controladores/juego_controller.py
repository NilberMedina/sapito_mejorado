import pygame
from logica.escena_logica import EscenaLogica
from grafica.mapa_grafico import MapaGrafico
from grafica.sapito_grafico import SapitoGrafico
from grafica.carro_grafico import CarroGrafico

class JuegoController:
    def __init__(self, tam_celda=60):
        self.tam_celda = tam_celda
        self.modelo = EscenaLogica()
        self.mapa_grafico = MapaGrafico(tam_celda)
        self.sapito_grafico = SapitoGrafico(tam_celda)
        self.carros_graficos = [CarroGrafico(tam_celda) for _ in self.modelo.carros]
    
    def manejar_evento(self, evento):
        if evento.type != pygame.KEYDOWN:
            return
        if evento.key == pygame.K_UP:
            self.modelo.sapito.moverArriba()
        elif evento.key == pygame.K_DOWN:
            self.modelo.sapito.moverAbajo(self.modelo.filas - 1)
        elif evento.key == pygame.K_LEFT:
            self.modelo.sapito.moverIzquierda()
        elif evento.key == pygame.K_RIGHT:
            self.modelo.sapito.moverDerecha(self.modelo.columnas - 1)
    
    def update(self):
        self.modelo.update()
        self.sapito_grafico.update()
    
    def render(self, pantalla):
        estado = self.modelo.getEstado()
        self.mapa_grafico.render(pantalla, estado['mapa'])
        for i, carro_pos in enumerate(estado['carros']):
            fila, columna = carro_pos
            self.carros_graficos[i].render(pantalla, fila, columna)
        fila, columna = estado['sapito']
        self.sapito_grafico.render(pantalla, fila, columna)
        
        self._render_info(pantalla, estado)
    
    def _render_info(self, pantalla, estado):
        font = pygame.font.Font(None, 24)