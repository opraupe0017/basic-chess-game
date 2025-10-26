class BasicChessGame():
    def __init__(self):
        pass # Implementar código desde esta línea
    
    def set_fichas(self):
        """Cargar las fichas en el tablero.
        """
        #Fichas de Peones Negros 
        self.tablero.set_ficha(Peon(posicion=['a', 7], es_blanco=False))
        self.tablero.set_ficha(Peon(posicion=['b', 7], es_blanco=False))
        self.tablero.set_ficha(Peon(posicion=['c', 7], es_blanco=False))
        self.tablero.set_ficha(Peon(posicion=['d', 7], es_blanco=False))
        self.tablero.set_ficha(Peon(posicion=['e', 7], es_blanco=False))
        self.tablero.set_ficha(Peon(posicion=['f', 7], es_blanco=False))
        self.tablero.set_ficha(Peon(posicion=['g', 7], es_blanco=False))
        self.tablero.set_ficha(Peon(posicion=['h', 7], es_blanco=False))

        #Fichas de Caballos Negros 
        self.tablero.set_ficha(caballo(posicion=['b', 8], es_blanco=False))
        self.tablero.set_ficha(caballo(posicion=['g', 8], es_blanco=False))

        #Fichas de las Torres Negras 
        self.tablero.set_fichas(Torre(posicion=['h', 8], es_blanco=False))
        self.tablero.set_fichas(Torre(posicion=['a', 8], es_blanco=False))

        #Fichas de Alfiles Negros
        self.tablero.set_ficha(Alfil(posicion=['c', 8], es_blanco=False))
        self.tablero.set_ficha(Alfil(posicion=['f', 8], es_blanco=False))

        #Ficha del Rey Negro
        self.tablero.set_ficha(Rey(posicion=["e", 8], es_blanco=False))

        #Ficha de la Reina Negra 
        self.tablero.set_ficha(reina(posicion=['d', 8], es_blanco=False))

        self.rey_negro = self.tablero["e8"]
    

    def jugar(self):
        """Activador del juego de ajedrez básico.
        """
        pass # Implementar código desde esta línea


if __name__ == '__main__':
    juego = BasicChessGame()
    print(juego.jugar())
