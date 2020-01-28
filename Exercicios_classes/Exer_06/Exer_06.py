class Televisor:

    def __init__(self, canal = 0, volume = 0 ):
        self.canal = canal
        self.volume = volume
    
    def altera_numero_canal(self, canal):
        if(self.canal_valido()):
            self.canal += canal
        else:
            print("Canal não localizado!")
        
    def aumentar_volume(self):
        if(self.volume_valido()):
            self.volume += 1
        else:
            print("Volume está no maximo!")

    def diminuir_volume(self):
        if(self.volume_valido()):
            self.volume -= 1
        else:
            print("Volume está no minino!")
    
    def volume_valido(self):
        if(self.volume >= 0 or self.volume <= 10):
            return True
        else: 
            return False
    
    def canal_valido(self):
        if(self.canal >= 0 or self.volume <= 100):
            return True
        else: 
            return False
    