class Quadrado:
    
    def __init__(self, medida):
        self.medida = medida
    
    def area(self):
        return self.medida ** 2
    
    def perimetro(self):
        return self.medida * 4

