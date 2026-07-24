class CarroLogica:
    
    def __init__(self, fila, columna, direccion=1, velocidad=15):
        self.fila = fila
        self.columna = columna
        self.direccion = direccion  
        self.velocidad = velocidad
        self._contador = 0
    
    def update(self, columnas):
        self._contador += 1
        if self._contador < self.velocidad:
            return
        self._contador = 0
        
        if self.direccion == 1:
            if self.columna >= columnas - 1:
                self.columna = 0
            else:
                self.columna += 1
        else:
            if self.columna <= 0:
                self.columna = columnas - 1
            else:
                self.columna -= 1
    
    def getPosicion(self):
        return (self.fila, self.columna)
    
    def setPosicion(self, fila, columna):
        self.fila = fila
        self.columna = columna