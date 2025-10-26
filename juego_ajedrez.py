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
        turno_blancos = True
        while self.rey_blanco.esta_activo ==  True and self.rey_negro.esta_activo == True:
            se_rinde = input("¿Deseas rendirte?")
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
                        turno_blancos = False
                    except:
                        print(f"Posición {hasta} fuera del tablero.")
        
        if self.rey_blanco.esta_activo == False:
            print("Ganador Rey negro")
        else:
            print("Ganador Rey blanco")         


if __name__ == '__main__':
    juego = BasicChessGame()
    print(juego.jugar())
