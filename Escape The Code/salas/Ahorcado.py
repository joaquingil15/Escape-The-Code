import random

# Lista de palabras relacionadas con la temática del Escape Room
palabras = ["CORAZON", "MIEDO", "INDEFINIDO", "SOLEDAD", "PODER",
            "ESTERNOCLEIDOMASTOIDEO", "ESCAPAR", "DOLORES", "PANICO", "LABURO"]

MAX_INTENTOS = 6

# Un dibujo por cada cantidad de errores cometidos: dibujos[0] es el patíbulo
# vacío, dibujos[MAX_INTENTOS] es el ahorcado completo (fin del juego).
# La lista tiene que tener MAX_INTENTOS + 1 elementos.
dibujos = ['''
 +---+
 |   |
     |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
 |   |
     |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
/    |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
=========''']


def elegir_palabra(lista):
    """Selecciona aleatoriamente una palabra de la lista."""
    return random.choice(lista)


def mostrar_ahorcado(errores):
    """Imprime el dibujo del ahorcado correspondiente a la cantidad de errores."""
    print(dibujos[errores])


def mostrar_progreso(palabra, descubiertas):
    """Arma el string con las letras descubiertas y guiones bajos para el resto."""
    progreso = ""
    for letra in palabra:
        if letra in descubiertas:
            progreso += letra + " "
        else:
            progreso += "_ "
    return progreso.strip()


def pedir_letra(usadas):
    """Pide una letra al jugador y la valida. Devuelve None si el ingreso no es válido
    (no cuenta como intento)."""
    entrada = input("Ingresá una letra: ").strip().upper()

    if len(entrada) != 1:
        print("⚠ Tenés que ingresar un único carácter.")
        return None

    if not entrada.isalpha():
        print("⚠ Tenés que ingresar una letra.")
        return None

    if entrada in usadas:
        print(f"⚠ Ya usaste la letra '{entrada}'. Probá con otra.")
        return None

    return entrada


def palabra_completa(palabra, descubiertas):
    """Indica si ya se descubrieron todas las letras de la palabra."""
    for letra in palabra:
        if letra not in descubiertas:
            return False
    return True


def mostrar_encabezado():
    print("""▌ ▌   ▜▜     ▌ ▌      ▜   ▌▐
▙▄▌▞▀▖▐▐ ▞▀▖ ▌▖▌▞▀▖▙▀▖▐ ▞▀▌▐
▌ ▌▛▀ ▐▐ ▌ ▌ ▙▚▌▌ ▌▌  ▐ ▌ ▌▝
▘ ▘▝▀▘ ▘▘▝▀  ▘ ▘▝▀ ▘   ▘▝▀▘▝ """)
    input("Presioná Enter para comenzar el juego...")


def jugar_ahorcado(lista):
    mostrar_encabezado()

    palabra = elegir_palabra(lista)
    print(f"La palabra tiene {len(palabra)} letras.")

    descubiertas = []   # letras correctas ya reveladas
    usadas = []          # todas las letras ya ingresadas (correctas e incorrectas)
    intentos_restantes = MAX_INTENTOS

    while intentos_restantes > 0:
        errores = MAX_INTENTOS - intentos_restantes
        print()
        mostrar_ahorcado(errores)
        print(mostrar_progreso(palabra, descubiertas))
        print(f"Intentos restantes: {intentos_restantes}")
        print(f"Letras usadas: {', '.join(usadas) if usadas else '(ninguna)'}")

        letra = pedir_letra(usadas)
        if letra is None:
            # ingreso inválido o letra repetida: no consume intento
            continue

        usadas.append(letra)

        if letra in palabra:
            descubiertas.append(letra)
            print(f"✔ ¡Bien! La letra '{letra}' está en la palabra.")
            if palabra_completa(palabra, descubiertas):
                print()
                print(mostrar_progreso(palabra, descubiertas))
                print(f"🎉 ¡Descubriste la palabra! Era: {palabra}")
                return True
        else:
            intentos_restantes -= 1
            print(f"✘ La letra '{letra}' no está en la palabra.")

    # se agotaron los intentos
    print()
    mostrar_ahorcado(MAX_INTENTOS)
    print(f"💀 Perdiste el desafío. La palabra era: {palabra}")
    return False


if __name__ == "__main__":
    jugar_ahorcado(palabras)