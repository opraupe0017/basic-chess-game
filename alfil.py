
class Alfil():
    def __init__(self,posición=['c', 1] es_blanco=True):
        self. es_blanco = es_blanco 
        self. posición = posición
        self. esta_activo = True 

def set_posición(self, posición_nueva): 
    letra = posición_nueva[0]
    número = posición_nueva[1] 

    letra_actual = ord(self.posición[0])
    numero_actual = self. posición[1]
    
    #Movimiento del Alfil 
    if abs(letra - letra_actual) == abs(número - numero_actual) and letra != letra_actual: 
        self.posición = posición_nueva 
    else:
        print('ERROR.Posición invalida')
