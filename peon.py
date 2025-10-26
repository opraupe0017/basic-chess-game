class Peon():
    def __init__(self, posicion=["a",2], es_blanco=True):
        self.es_blanco = es_blanco
        self.posicion = posicion
        self.esta_activo = True

    def set_posicion(self, posicion_nueva):
        letra = ord(posicion_nueva[0])
        numero = posicion_nueva[1]

        letra_actual = ord(self.posicion[0])
        numero_actual = self.posicion[1]

        num = 1 if self.es_blanco else -1
        if (numero_actual + num) == numero and letra_actual == letra:
            self.posicion = posicion_nueva
        elif (numero_actual + num) == numero and abs(letra - letra_actual) == 1:
            self.posicion = posicion_nueva
        else:
            raise Exception("ERROR, posicion invalida. ")

    def __str__(self):
        return "♙" if self.es_blanco else "♟"
        
