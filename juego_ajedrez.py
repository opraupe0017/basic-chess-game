from peon import Peon
from torre import Torre
from caballo import Caballo
from rey import Rey
from reina import reina
from alfil import Alfil 



class BasicChessGame():
    def __init__(self):
        pass # Implementar código desde esta línea
    
    def set_fichas(self): 
        """Cargar las fichas en el tablero.
        """
        pass # Implementar código desde esta línea

    def jugar(self):
        """Activador del juego de ajedrez básico.
        """
        
        #FichasBlancas
        self.tablero.set_ficha(Torre(['a', 1], True))
        self.tablero.set_ficha(Caballo(['b', 1], True))
        self.tablero.set_ficha(Alfil(['c', 1], True))
        self.tablero.set_ficha(reina(['d', 1], True))
        self.tablero.set_ficha(Rey(['e', 1], True))
        self.tablero.set_ficha(Alfil(['f', 1], True))
        self.tablero.set_ficha(Caballo(['g', 1], True))
        self.tablero.set_ficha(Torre(['h', 1], True))
        #Peones Blancos
        self.tablero.set_ficha(Peon['a', 2, True])
        self.tablero.set_ficha(Peon['b', 2, True])
        self.tablero.set_ficha(Peon['c', 2, True])
        self.tablero.set_ficha(Peon['d', 2, True])
        self.tablero.set_ficha(Peon['e', 2, True])
        self.tablero.set_ficha(Peon['f', 2, True])
        self.tablero.set_ficha(Peon['g', 2, True])
        self.tablero.set_ficha(Peon['h', 2, True])
        

        self.rey_blanco = self.tablero['e1']



if __name__ == '__main__':
    juego = BasicChessGame()
    print(juego.jugar())
