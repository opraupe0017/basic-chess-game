class reina():
    def __init__(self, posicion=['d', 1], es_blanco=True):
        self.es_blanco = es_blanco
        self.posicion = posicion
        self.esta_activo = True

    def set_posicion(self, posicion_nueva):
        letra = ord(posicion_nueva[0])
        numero = posicion_nueva[1]

        letra_actual = ord(self.posicion[0])
        numero_actual = self.posicion[1]

        if(letra_actual == letra and numero_actual != numero:) or \
                (letra_actual != letra and numero_actual == numero):
            self.posicion = posicion_nueva
        elif abs(letra - letra_actual) == abs(numero - numero_actual) \
                and letra != letra_actual:
            self.posicion = posicion_nueva
        else:
            print("Movimiento inválido para la reina.")

        
