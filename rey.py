class Rey:
    def __init__(self, posicion=['e', 1], es_blanco=True):
        self.es_blanco = es_blanco
        self.posicion = posicion
        self.esta_activo = True

    def set_posicion(self, posicion_nueva):
        letra = ord(posicion_nueva[0])
        numero = posicion_nueva[1]

        letra_actual = ord(self.posicion[0])
        numero_actual = self.posicion[1]

        # Movimiento en una sola casilla horizontal, vertical o diagonal
        if abs(letra - letra_actual) <= 1 and abs(numero - numero_actual) <= 1:
            if letra != letra_actual or numero != numero_actual:  # No se queda quieto
                self.posicion = posicion_nueva
            else:
                print("El rey debe moverse al menos una casilla.")
        else:
            print("Movimiento inválido para el rey.")

    def __str__(self):
        return "♔" if self.es_blanco else "♚"
    
if __name__ == "__main__":
    reicito = Rey(posicion=['e', 8], es_blanco=True)
    print(reicito.posicion)
    reicito.set_posicion(posicion_nueva=['d', 7])
    print(reicito.posicion)
    print(reicito)

    reicito.set_posicion(posicion_nueva=['f', 5])
    print(reicito.posicion)



    
