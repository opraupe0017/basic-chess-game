from peon import Peon
from torre import Torre
from caballo import Caballo


class Tablero():
    def __init__(self):
        self.fichas = {}
        self.movimientos = []
    
    def set_ficha(self, ficha):
        """Asigna una ficha al tablero

        Args:
            ficha: Objeto de clase Rey, Reina, Torre, Alfil, Caballo o Peon.
        """
        letra = ficha.posicion[0]
        numero = ficha.posicion[1]
        posicion = f'{letra}{numero}'
        self.fichas[posicion] = ficha
    
    def set_mover(self, desde, hasta):
        """Mueve la ficha desde una posición a otra.
        En caso de que se encuentre una ficha del rival en la
        posición de destino, la elimina.

        Args:
            desde (str, optional): Posición de la ficha actual. Defaults to 'b1'.
            hasta (str, optional): Posición de la ficha destino. Defaults to 'c3'.

        Raises:
            Exception: Error de posición desde o hasta fuera del tablero.
            Exception: Error de tratar de eliminar una ficha del mismo bando.
        """
        pieza = self.fichas.get(desde)
        destino = self.fichas.get(hasta)
    
        if not pieza:
            raise Exception("No hay ficha en la posición inicial.")

        # Verificar límites del tablero
        letra_desde = desde[0]
        numero_desde = int(desde[1])
        
        letra_hasta = hasta [0]
        numero_hasta = int(hasta [1])
        
        con_1 = "a" <= letra_desde <= "h" and 1 <= numero_desde <= 8
        con_2 = "a" <= letra_hasta <= "h" and 1 <= numero_hasta <= 8
        if not (con_1 and con_2):
            raise Exception("Posición fuera del tablero.")

       
        # Si hay una pieza en el destino
        if destino:
            if destino.es_blanco == pieza.es_blanco:
                raise Exception("No puedes capturar una pieza del mismo bando.")
            else:
                # Eliminar pieza rival
                self.fichas[hasta].esta_activo = False
                
        # Verificar movimiento válido según la pieza
        self.fichas[desde].set_posicion([letra_hasta, numero_hasta])
        self.movimientos.append(f"{desde}->{hasta}")
    
    def __str__(self):
        """Muestra el tablero de ajedrez con las fichas en las posiciones actuales
           _ _ _ _ _ _ _ _
        8 |_|_|_|_|_|_|_|_|
        7 |_|_|_|_|_|_|_|_|
        6 |_|_|_|_|_|_|_|_|
        5 |_|_|_|_|_|_|_|_|
        4 |_|_|_|_|_|_|_|_|
        3 |_|_|_|_|_|_|_|_|
        2 |_|_|_|_|_|_|_|_|
        1 |_|_|_|_|_|_|_|_|
           a b c d e f g h
        """
        tablero = '   _ _ _ _ _ _ _ _\n'
        for i in range(8):
            tablero += f'{8 - i} |'
            for j in range(8):
                if f'{chr(97 + j)}{8 - i}' in self.fichas:
                    tablero += f'{str(self.fichas[f'{chr(97 + j)}{8 - i}'])}|'
                else:
                    tablero += '_|'
            tablero += '\n'
        tablero += '   a b c d e f g h'
        return tablero

if __name__ == '__main__':
    from caballo import Caballo


    tablero = Tablero()
    fichas = [
        Caballo(posicion=['b', 1], es_blanco=True),
        Caballo(posicion=['g', 1], es_blanco=True),
        Caballo(posicion=['a', 4], es_blanco=False),
        Caballo(posicion=['g', 8], es_blanco=False)
    ]
    for ficha in fichas:
        tablero.set_ficha(ficha)
    print(tablero)

    tablero.set_mover('g1', 'e2')
    print(tablero)
    tablero.set_mover('a4', 'c3')
    print(tablero)
    tablero.set_mover('b1', 'c3')
    print(tablero)
    tablero.set_mover('g8', 'h6')
    print(tablero)
    print(tablero.movimientos)
    # Un caballo blanco tratando de eliminar otro caballo blanco
    tablero.set_mover('e2', 'c3')
    print(tablero)
