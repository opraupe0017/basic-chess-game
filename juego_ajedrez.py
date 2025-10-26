from tablero import Tablero

class BasicChessGame():
    def __init__(self):
        self.tablero = Tablero()
        self.rey_blanco = None
        self.rey_negro = None
    
    def set_fichas(self):
        """Cargar las fichas en el tablero.
        """
        pass # Implementar código desde esta línea

    def jugar(self):
        """Activador del juego de ajedrez básico.
        """
        pass # Implementar código desde esta línea


if __name__ == '__main__':
    juego = BasicChessGame()
    print(juego.jugar())
