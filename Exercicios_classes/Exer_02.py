class Quadrado:
    
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def mudar_valor_do_lado(self, valor):
        self.tamanho_do_lado = valor
    
    def retorna_valor_do_lado(self):
        return self.tamanho_do_lado
    
    def calcula_area(self):
        area = self.tamanho_do_lado * self.tamanho_do_lado
        return area