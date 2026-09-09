import random

# Crear tablero 5x5
def crear_tablero():
    tablero = []
    for i in range(5):
        fila = []
        for j in range(5):
            fila.append("-")
        tablero.append(fila)
    return tablero


# Verifica si una posición es válida para poner un barco
def posicion_valida(barcos, fila, columna):
    for barco in barcos:
        f_barco = barco[0]
        c_barco = barco[1]

        if abs(f_barco - fila) <= 1 and abs(c_barco - columna) <= 1:
            return False

    return True


# Generar 3 barcos
def generar_barcos():
    barcos = []

    while len(barcos) < 3:
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)

        if posicion_valida(barcos, fila, columna):
            barcos.append([fila, columna])

    return barcos


# Mostrar tablero visible al jugador
def mostrar_tablero(tablero):
    print("\n  0 1 2 3 4")

    for i in range(5):
        print(i, end=" ")
        for j in range(5):
            print(tablero[i][j], end=" ")
        print()


# Juego principal
def mini_batalla_naval():
    tablero = crear_tablero()
    barcos = generar_barcos()

    disparos = 10
    hundidos = 0

    while disparos > 0 and hundidos < 3:

        mostrar_tablero(tablero)

        print("\nBarcos hundidos:", hundidos)
        print("Barcos restantes:", 3 - hundidos)
        print("Disparos disponibles:", disparos)

        fila = int(input("Fila (0-4): "))
        columna = int(input("Columna (0-4): "))

        # Validar rango
        if fila < 0 or fila > 4 or columna < 0 or columna > 4:
            print("Coordenadas inválidas.")
            continue

        # Validar repetido
        if tablero[fila][columna] != "-":
            print("Ya disparaste ahí.")
            continue

        impacto = False

        for barco in barcos:
            if barco[0] == fila and barco[1] == columna:
                impacto = True

        if impacto:
            print("¡IMPACTO! Barco hundido.")
            tablero[fila][columna] = "X"
            hundidos += 1
        else:
            print("AGUA")
            tablero[fila][columna] = "O"

        disparos -= 1

    if hundidos == 3:
        print("\n¡GANASTE LA SALA 2!")
    else:
        print("\nPERDISTE LA SALA 2")
        print("Los barcos estaban en:")
        print(barcos)


# Prueba
mini_batalla_naval()