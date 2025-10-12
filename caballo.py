class Caballo():
    def __init__(self, posicion=['b', 1], es_blanco=True):
        self.es_blanco = es_blanco
        self.posicion = posicion
        self.esta_activo = True
    
    def set_posicion(self, posicion_nueva):
        letra_nuevo = ord(posicion_nueva[0])
        numero_nuevo = posicion_nueva[1]

        letra_actual = ord(self.posicion[0])
        numero_actual = self.posicion[1]

        # Movimiento del caballo
        cond_1 = abs(letra_nuevo - letra_actual) == 1 and abs(numero_nuevo - numero_actual) == 2
        cond_2 = abs(letra_nuevo - letra_actual) == 2 and abs(numero_nuevo - numero_actual) == 1
        if cond_1 or cond_2:
            self.posicion[0] = posicion_nueva[0]
            self.posicion[1] = posicion_nueva[1]
        else:
            # generar mensaje de error de posición no válida con raise
            raise Exception(f'ERROR: Posición no válida. El caballo no se puede mover de {self.posicion[0]}{self.posicion[1]} a {posicion_nueva[0]}{posicion_nueva[1]}.')
        
    def set_estado(self, esta_activo):
        self.esta_activo = esta_activo
    
    def __str__(self):
        return '♘' if self.es_blanco else '♞'


if __name__ == '__main__':
    caballo = Caballo(posicion=['b', 1], es_blanco=True)
    print(caballo)
    caballo.set_posicion(['c', 3])
    print(caballo)
    # caballo.set_posicion(['b', 3])
    # print(caballo)
