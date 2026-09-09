import random

def mostrar_ahorcado(errores):
    """Imprime el dibujo del ahorcado dependiendo de la cantidad de errores.
    
    Parametros:
        errores (int): cantidad de errores cometidos (0 a 6 (max_intentos))
    """
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
========='''] #dibujos dependiendo de la cantidad de errores, modo clasico son 6.
    print(dibujos[errores])



def mostrar_progreso(palabra, descubiertas):
    """Arma el string con las letras descubiertas y guiones bajos para el resto.
    
    Parametros:
        palabra (str): la palabra a adivinar
        descubiertas (list): lista de letras ya descubiertas
    
    Retorna:
        str: el progreso del jugador, con letras descubiertas y guiones bajos

    """
    progreso = ""
    for letra in palabra:
        if letra in descubiertas: #si la letra esta en la lista de descubiertas, se agrega a progreso
            progreso += letra + " "
        else:
            progreso += "_ "
    return progreso.strip()


def pedir_letra(usadas):
    """Pide una letra al jugador y la valida.
    
    Parametros:
        usadas (list): lista de letras ya ingresadas.
    
    Retorna:
        str or None: la letra ingresada si es valida, None si es invalida.
    """
    entrada = input("Ingrese una letra: ").strip().upper()
    print()

    if len(entrada) != 1:
        print("Error - Tienes que ingresar una letra sola.")
        return None

    if not entrada.isalpha():
        print("Error - Tienes que ingresar una letra.")
        return None

    if entrada in usadas:
        print(f"Error - Ya uso la letra '{entrada}'. Pruebe con otra.")
        return None

    return entrada

def palabra_completa(palabra, descubiertas):
    """Indica si ya se descubrieron todas las letras de la palabra.
    
    Parametros:
        palabra (str): la palabra a adivinar
        descubiertas (list): lista de letras ya descubiertas
    
    Retorna:
        bool: True si todas las letras de la palabra estan descubiertas, False si no es asi.
    """
    for letra in palabra:
        if letra not in descubiertas:
            return False
    return True

def jugar_ahorcado():
    """ Función principal del juego del ahorcado.

    Retorna:
        bool: True si el jugador adivino la palabra, False si perdio.
    """
    print("""▌ ▌   ▜▜     ▌ ▌      ▜   ▌▐
▙▄▌▞▀▖▐▐ ▞▀▖ ▌▖▌▞▀▖▙▀▖▐ ▞▀▌▐
▌ ▌▛▀ ▐▐ ▌ ▌ ▙▚▌▌ ▌▌  ▐ ▌ ▌▝
▘ ▘▝▀▘ ▘▘▝▀  ▘ ▘▝▀ ▘   ▘▝▀▘▝ """)
    input("Presioná Enter para comenzar el juego...")

    palabras = ["CORAZON", "MIEDO", "INDEFINIDO", "SOLEDAD", "PODER",
            "ESTERNOCLEIDOMASTOIDEO", "ESCAPAR", "DOLORES", "PANICO", "LABURO"]
    palabra = random.choice(palabras)

    print(f"La palabra tiene {len(palabra)} letras.")

    max_intentos = 6    
    descubiertas = []   # letras correctas
    usadas = []          # todas las letras ingresadas (correctas e incorrectas)
    intentos_restantes = max_intentos

    while intentos_restantes > 0:
        errores = max_intentos - intentos_restantes
        print()
        mostrar_ahorcado(errores)
        print(mostrar_progreso(palabra, descubiertas))
        print(f"Intentos restantes: {intentos_restantes}")
        print(f"Letras usadas: {', '.join(usadas) if usadas else '(ninguna)'}") #join muestra una "," entr cada letra en la lista usadas, else (Si no hay letras en la lista) muestra "(ninguna)" 

        letra = pedir_letra(usadas)
        if letra is None:
            # ingreso invalido o letra ya usada: no usa un intento.
            continue

        usadas.append(letra)

        if letra in palabra:
            descubiertas.append(letra)
            print(f" Correcto...")
            if palabra_completa(palabra, descubiertas):
                print()
                print(mostrar_progreso(palabra, descubiertas))
                print(f" Has descubierto la palabra {palabra} y Puedes pasar a la siguiente sala.")
                return True
        else:
            intentos_restantes -= 1
            print(f"X La letra '{letra}' no está en la palabra.")

    # se agotaron los intentos
    print()
    mostrar_ahorcado(max_intentos)
    print(f"Perdiste, no vas a poder continuar sin ganar un ahorcado. La palabra era: {palabra}")
    return False