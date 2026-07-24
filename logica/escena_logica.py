from logica.sapito_logica import SapitoLogica
from logica.carro_logica import CarroLogica

class EscenaLogica:
    
    M = "M" 
    P = "P" 
    V = "V" 
    A = "A" 
    
    def __init__(self):
        self.mapa = [
            [self.M, self.M, self.M, self.M, self.M, self.M, self.M, self.M, self.M, self.M, self.M, self.M],
            [self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P],
            [self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P],
            [self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P],
            [self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P],
            [self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P],
            [self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P],
            [self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P, self.P],
            [self.V, self.V, self.V, self.V, self.V, self.V, self.V, self.V, self.V, self.V, self.V, self.V],
            [self.A, self.A, self.A, self.A, self.A, self.A, self.A, self.A, self.A, self.A, self.A, self.A],
        ]
        
        self.filas = len(self.mapa)
        self.columnas = len(self.mapa[0])
        
        self.sapito = SapitoLogica(9, 6)
        
        self.carros = [
            CarroLogica(1, 3, direccion=1),
            CarroLogica(2, 2, direccion=-1),
            CarroLogica(3, 5, direccion=1),
            CarroLogica(4, 5, direccion=-1),
            CarroLogica(5, 8, direccion=1),
            CarroLogica(6, 1, direccion=-1),
            CarroLogica(7, 4, direccion=1),
        ]
    
    def update(self):
        for carro in self.carros:
            carro.update(self.columnas)
        
    def getEstado(self):
        return {
            'mapa': self.mapa,
            'sapito': self.sapito.getPosicion(),
            'carros': [carro.getPosicion() for carro in self.carros],
        }