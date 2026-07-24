class SapitoLogica:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.vida = True
        self.puntaje = True
    
    def moverArriba(self):
        if self.fila > 0:
            self.fila -= 1
            return True
        return False
    
    def moverAbajo(self, fila_max):
        if self.fila < fila_max:
            self.fila += 1
            return True
        return False
    
    def moverIzquierda(self):
        if self.columna > 0:
            self.columna -= 1
            return True
        return False
    
    def moverDerecha(self, columna_max):
        if self.columna < columna_max:
            self.columna += 1
            return True
        return False
    
    def getPosicion(self):
        return (self.fila, self.columna)
    
    def setPosicion(self, fila, columna):
        self.fila = fila
        self.columna = columna