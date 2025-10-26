from tablero import Tablero
from peon import Peon
from torre import Torre
from caballo import Caballo
from rey import Rey
from reina import reina
from alfil import Alfil 


class BasicChessGame():
    def __init__(self):
        self.tablero = Tablero()
        self.rey_blanco = None
        self.rey_negro = None
    
    def set_fichas(self): 
        """Cargar las fichas en el tablero.
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
        self.tablero.set_ficha(Peon(['a', 2], True))
        self.tablero.set_ficha(Peon(['b', 2], True))
        self.tablero.set_ficha(Peon(['c', 2], True))
        self.tablero.set_ficha(Peon(['d', 2], True))
        self.tablero.set_ficha(Peon(['e', 2], True))
        self.tablero.set_ficha(Peon(['f', 2], True))
        self.tablero.set_ficha(Peon(['g', 2], True))
        self.tablero.set_ficha(Peon(['h', 2], True))

        self.rey_blanco = self.tablero.fichas['e1']

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
        self.tablero.set_ficha(Caballo(posicion=['b', 8], es_blanco=False))
        self.tablero.set_ficha(Caballo(posicion=['g', 8], es_blanco=False))

        #Fichas de las Torres Negras 
        self.tablero.set_ficha(Torre(posicion=['h', 8], es_blanco=False))
        self.tablero.set_ficha(Torre(posicion=['a', 8], es_blanco=False))

        #Fichas de Alfiles Negros
        self.tablero.set_ficha(Alfil(posicion=['c', 8], es_blanco=False))
        self.tablero.set_ficha(Alfil(posicion=['f', 8], es_blanco=False))

        #Ficha del Rey Negro
        self.tablero.set_ficha(Rey(posicion=["e", 8], es_blanco=False))

        #Ficha de la Reina Negra 
        self.tablero.set_ficha(reina(posicion=['d', 8], es_blanco=False))

        self.rey_negro = self.tablero.fichas["e8"]

    def jugar(self):
        """Activador del juego de ajedrez básico.
        """
        self.set_fichas()
        turno_blancos = True
        while self.rey_blanco.esta_activo ==  True and self.rey_negro.esta_activo == True:
            print(self.tablero)
            se_rinde = input("¿Deseas rendirte? ")
            if se_rinde == "si" and turno_blancos == True:
                self.rey_blanco.esta_activo = False
            elif se_rinde == "si" and turno_blancos == False:
                self.rey_negro.esta_activo = False
            else:
                desde = input("Ingresa posicion desde: ")
                hasta = input("Ingresa posicion hasta: ")
                cond_1 = self.tablero.fichas.get(desde,None) is not None
                cond_2 = self.tablero.fichas[desde].es_blanco == turno_blancos
                if cond_1 and cond_2:
                    try:
                        self.tablero.set_mover(desde, hasta)
                        turno_blancos = not turno_blancos
                    except:
                        print(f"Posición {hasta} fuera del tablero.")
        
        if self.rey_blanco.esta_activo == False:
            return "Ganador Rey negro"
        else:
            return "Ganador Rey blanco"


if __name__ == '__main__':
    juego = BasicChessGame()
    print(juego.jugar())
