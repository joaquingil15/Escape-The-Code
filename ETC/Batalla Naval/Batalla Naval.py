import random


# ---------- TABLERO ----------

def crear_tablero():
    """Crea una matriz 5x5 vacía, representada con '-'."""
    tablero = []
    for i in range(5):
        fila = []
        for j in range(5):
            fila.append("-")
        tablero.append(fila)
    return tablero


def mostrar_tablero(tablero):
    """Muestra el tablero visible para el jugador."""
    print("\n  0 1 2 3 4")
    for i in range(5):
        print(i, end=" ")
        for j in range(5):
            print(tablero[i][j], end=" ")
        print()


# ---------- GENERACIÓN DE BARCOS ----------

def posicion_valida(barcos, fila, columna):
    """
    Verifica que la posición no esté ocupada ni sea adyacente
    (horizontal, vertical o diagonal) a un barco ya ubicado.
    """
    for barco in barcos:
        f_barco = barco[0]
        c_barco = barco[1]
        if abs(f_barco - fila) <= 1 and abs(c_barco - columna) <= 1:
            return False
    return True


def generar_barcos(cantidad=3):
    """Genera 'cantidad' barcos en posiciones válidas y no adyacentes."""
    barcos = []
    while len(barcos) < cantidad:
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)
        if posicion_valida(barcos, fila, columna):
            barcos.append([fila, columna])
    return barcos


# ---------- ENTRADA Y VALIDACIÓN ----------

def pedir_numero(mensaje):
    """
    Pide un número por teclado. Si el usuario ingresa algo que no es
    un número, devuelve None en lugar de romper el programa.
    """
    entrada = input(mensaje).strip()
    if not entrada.isdigit():
        return None
    return int(entrada)


def coordenada_en_rango(fila, columna):
    """Verifica que fila y columna estén dentro del tablero (0 a 4)."""
    return 0 <= fila <= 4 and 0 <= columna <= 4


def posicion_ya_atacada(tablero, fila, columna):
    """Verifica si esa posición ya fue disparada anteriormente."""
    return tablero[fila][columna] != "-"


# ---------- LÓGICA DEL DISPARO ----------

def hay_impacto(barcos, fila, columna):
    """Determina si en (fila, columna) hay un barco."""
    for barco in barcos:
        if barco[0] == fila and barco[1] == columna:
            return True
    return False


def procesar_disparo(tablero, barcos, fila, columna):
    """
    Aplica el resultado del disparo sobre el tablero y devuelve
    True si fue impacto, False si fue agua.
    """
    if hay_impacto(barcos, fila, columna):
        tablero[fila][columna] = "X"
        print("¡IMPACTO! Barco hundido.")
        return True
    else:
        tablero[fila][columna] = "O"
        print("AGUA")
        return False


# ---------- INFORMACIÓN DE ESTADO ----------

def mostrar_estado(hundidos, total_barcos, disparos):
    """Muestra el resumen luego de cada jugada."""
    print("\nBarcos hundidos:", hundidos)
    print("Barcos restantes:", total_barcos - hundidos)
    print("Disparos disponibles:", disparos)


def formatear_barcos(barcos):
    """Devuelve las coordenadas de los barcos en formato legible."""
    textos = []
    for barco in barcos:
        texto = "(" + str(barco[0]) + "," + str(barco[1]) + ")"
        textos.append(texto)
    return ", ".join(textos)


# ---------- JUEGO PRINCIPAL ----------

def mini_batalla_naval():
    tablero = crear_tablero()
    total_barcos = 3
    barcos = generar_barcos(total_barcos)

    disparos = 10
    hundidos = 0

    while disparos > 0 and hundidos < total_barcos:
        mostrar_tablero(tablero)
        print("\nDisparos restantes:", disparos)

        fila = pedir_numero("Fila (0-4): ")
        columna = pedir_numero("Columna (0-4): ")

        if fila is None or columna is None:
            print("Debe ingresar un número.")
            continue

        if not coordenada_en_rango(fila, columna):
            print("Coordenadas fuera de rango.")
            continue

        if posicion_ya_atacada(tablero, fila, columna):
            print("Ya disparaste ahí. Elegí otra posición.")
            continue

        impacto = procesar_disparo(tablero, barcos, fila, columna)
        if impacto:
            hundidos += 1
        disparos -= 1

        mostrar_estado(hundidos, total_barcos, disparos)

    mostrar_tablero(tablero)

    if hundidos == total_barcos:
        print("\n¡GANASTE LA SALA 2!")
    else:
        print("\nPERDISTE LA SALA 2")
        print("Los barcos estaban en:", formatear_barcos(barcos))


if __name__ == "__main__":
    mini_batalla_naval()
