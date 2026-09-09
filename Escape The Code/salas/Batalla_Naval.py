import random

# Letras que identifican cada columna del tablero (índice 0 a 4)
COLUMNAS = ["A", "B", "C", "D", "E"]


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
    """Muestra el tablero visible para el jugador, con columnas A-E y filas 1-5."""
    print("\n  ", end="")
    for letra in COLUMNAS:
        print(letra, end=" ")
    print()

    for i in range(5):
        numero_fila = i + 1
        print(numero_fila, end=" ")
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
        f_barco = barco[0] # Fila del barco
        c_barco = barco[1] # Columna del barco
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

def pedir_columna(mensaje):
    """
    Pide una letra de columna (A a E). Si no es una letra válida,
    devuelve None en lugar de romper el programa.
    """
    entrada = input(mensaje).strip().upper()
    if entrada in COLUMNAS:
        return COLUMNAS.index(entrada)
    else:
        return None


def pedir_fila(mensaje):
    """
    Pide un número de fila (1 a 5). Si no es un número válido dentro
    del rango, devuelve None en lugar de romper el programa.
    """
    entrada = input(mensaje).strip()
    if not entrada.isdigit():
        return None

    numero = int(entrada)
    if numero < 1 or numero > 5:
        return None

    return numero - 1


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
    """Devuelve las coordenadas de los barcos en formato letra+número, ej: A1."""
    textos = []
    for barco in barcos:
        letra_columna = COLUMNAS[barco[1]]
        numero_fila = barco[0] + 1
        texto = letra_columna + str(numero_fila)
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

        columna = pedir_columna("Columna (A-E): ")
        if columna is None:
            print("Columna inválida. Debe ser una letra entre A y E.")
            continue

        fila = pedir_fila("Fila (1-5): ")
        if fila is None:
            print("Fila inválida. Debe ser un número entre 1 y 5.")
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
        return True
    else:
        print("\nPERDISTE LA SALA 2")
        print("Los barcos estaban en:", formatear_barcos(barcos))
        return False

