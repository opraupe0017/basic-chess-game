
class Alfil():
    def __init__(self, posicion=['c', 1], es_blanco=True):
        self.es_blanco = es_blanco 
        self.posicion = posicion
        self. esta_activo = True 

    def set_posicion(self, posicion_nueva): 
        letra = posicion_nueva[0]
        numero = posicion_nueva[1] 

        letra_actual = ord(self.posicion[0])
        numero_actual = self. posicion[1]
        
        #Movimiento del Alfil 
        if abs(letra - letra_actual) == abs(numero - numero_actual) and letra != letra_actual: 
            self.posicion = posicion_nueva 
        else:
            print('ERROR.Posición invalida')
    
    def __str__(self):
        return "♗" if self.es_blanco else "♝"
