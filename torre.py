class Torre:
    def __init__(self, posicion=('a', 1), es_blanco=True):
        self.posicion = posicion
        self.es_blanco = es_blanco
        self.esta_activo = True

    def set_posicion(self, posicion_nueva):
        letra_actual = self.posicion[0]
        numero_actual = self.posicion[1]
        letra_nueva = posicion_nueva[0]
        numero_nueva = posicion_nueva[1]

        # Movimiento válido: misma columna (letra) o misma fila (número)
        if (letra_actual == letra_nueva and numero_actual != numero_nueva) or \
                (letra_actual != letra_nueva and numero_actual == numero_nueva):
            self.posicion = posicion_nueva
        
        else:
            print("❌ Movimiento inválido para la torre.")

# ----------------------------
# PROGRAMA PRINCIPAL
# ----------------------------
torre = Torre(('d', 4))
print(f"Posición inicial de la torre: {torre.posicion}")

while True:
    letra = input("Ingrese la letra (a-h) o 'salir' para terminar: ").lower()
    if letra == "salir":
        print("Juego terminado.")
        break

    try:
        numero = int(input("Ingrese el número (1-8): "))
    except ValueError:
        print("⚠️ Número inválido. Intenta de nuevo.")
        continue

    # Validar rango del tablero
    if letra not in 'abcdefgh' or not (1 <= numero <= 8):
        print("⚠️ Coordenada fuera del tablero. Intenta de nuevo.")
        continue

    # Mover la torre
    torre.set_posicion((letra, numero))
