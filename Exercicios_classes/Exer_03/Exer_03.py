class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def mudar_valor_do_lado(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def retorna_lado(self):
        return self.comprimento, self.largura
    
    def calcular_area(self):
        area = self.comprimento * self.largura
        return area

    def calcular_perimetro(self):
        perimetro = 2 * (self.comprimento + self.largura)
        return perimetro 
