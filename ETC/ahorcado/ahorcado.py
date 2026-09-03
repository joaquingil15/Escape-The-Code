import random

def ahorcado(lista):
    print("""▌ ▌   ▜▜     ▌ ▌      ▜   ▌▐ 
▙▄▌▞▀▖▐▐ ▞▀▖ ▌▖▌▞▀▖▙▀▖▐ ▞▀▌▐ 
▌ ▌▛▀ ▐▐ ▌ ▌ ▙▚▌▌ ▌▌  ▐ ▌ ▌▝ 
▘ ▘▝▀▘ ▘▘▝▀  ▘ ▘▝▀ ▘   ▘▝▀▘▝ """)
    eleccion = random.choice(lista)
    print("La palabra tiene", len(eleccion), "letras.")
    print("_ " * len(eleccion))


palabras = ["CORAZON","MIEDO","INDEFINIDO","SOLEDAD","PODER","ESTERNOCLEIDOMASTOIDEO","ESCAPAR","DOLORES","PANICO","LABURO"]
ahorcado(palabras)