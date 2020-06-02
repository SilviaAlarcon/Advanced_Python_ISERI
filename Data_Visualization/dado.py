from random import randint

class Dado:
    """Clase que simula un dado"""
    
    def __init__(self,num_lados = 6):
        '''De manera predeterminada el dado tiene 6 caras'''
        self.num_caras = num_lados
        
    def tira_dados(self):
        '''Regresa el valor después de lanzar el dado'''
        return randint(1,self.num_caras)