class Rey:
    def __init__(self, posicion=['e', 1], es_blanco=True):
        # Posición inicial del rey: columna (letra), fila (número)
        self.posicion = posicion
        self.es_blanco = es_blanco

    def mover(self, direccion):
        # Columnas del tablero
        columnas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        # Extrage la columna y la fila actuales
        columna_actual = self.posicion[0]
        fila_actual = self.posicion[1]
        # Convertí la letra de columna a un número (índice)
        indice_columna = columnas.index(columna_actual)

        # Se hace movimientos posibles según la dirección
        if direccion == "adelante":
            nueva_fila = fila_actual + 1
            nueva_columna = columna_actual

        elif direccion == "atrás":
            nueva_fila = fila_actual - 1
            nueva_columna = columna_actual

        elif direccion == "izquierda":
            nueva_columna = columnas[indice_columna - 1] if indice_columna > 0 else None
            nueva_fila = fila_actual

        elif direccion == "derecha":
            nueva_columna = columnas[indice_columna + 1] if indice_columna < 7 else None
            nueva_fila = fila_actual

        elif direccion == "adelante izquierda":
            nueva_columna = columnas[indice_columna - 1] if indice_columna > 0 else None
            nueva_fila = fila_actual + 1

        elif direccion == "adelante derecha":
            nueva_columna = columnas[indice_columna + 1] if indice_columna < 7 else None
            nueva_fila = fila_actual + 1

        elif direccion == "atrás izquierda":
            nueva_columna = columnas[indice_columna - 1] if indice_columna > 0 else None
            nueva_fila = fila_actual - 1

        elif direccion == "atrás derecha":
            nueva_columna = columnas[indice_columna + 1] if indice_columna < 7 else None
            nueva_fila = fila_actual - 1

        else:
            print("Dirección no válida.")
            return

        # Valido que no salga del tablero
        if nueva_columna and 1 <= nueva_fila <= 8:
            self.posicion = [nueva_columna, nueva_fila]
            print(f"Rey movido a {nueva_columna}{nueva_fila}")
        else:
            print("Movimiento inválido, fuera del tablero.")


if __name__ == "__main__":
    rey = Rey()
    rey.mover("derecha")
    rey.mover("adelante izquierda")
    

