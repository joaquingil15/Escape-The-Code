import re

def encriptado(contra):
    resultado = ""
    for caracter in contra:
        codigo= ord(caracter)
        n_cod = codigo + 4
        resultado += chr(n_cod)
    return resultado

def requisitos(nueva_contra, contra1):
    """Valida la nueva contraseña. Devuelve True si es válida, False si no
    (e imprime qué requisito faltó)."""
    if len(nueva_contra) < 8:
        print("Error - debe tener al menos 8 caracteres.")
        return False

    if re.search(r"\s", nueva_contra):
        print("Error - no puede contener espacios.")
        return False

    if not re.search(r"[A-Z]", nueva_contra):
        print("Error - debe contener al menos una letra mayúscula.")
        return False

    if not re.search(r"[a-z]", nueva_contra):
        print("Error - debe contener al menos una letra minúscula.")
        return False

    if not re.search(r"\d", nueva_contra):
        print("Error - debe contener al menos un número.")
        return False

    if not re.search(r"[^A-Za-z0-9\s]", nueva_contra):
        print("Error - debe contener al menos un carácter especial.")
        return False

    if encriptado(nueva_contra) == contra1:
        print("Error - debe ser diferente de la contraseña actual.")
        return False

    return True

def cambiar_contraseña(contra1):
    log_pasword = input("Ingrese su contraseña actual: ")
    log_pasword = encriptado(log_pasword)

    if log_pasword != contra1:
        print("Error - Contraseña incorrecta")
        return contra1

    while True:
        nueva_contra = input("Ingrese su nueva contraseña: ")
        if requisitos(nueva_contra, contra1):
            print("Contraseña cambiada exitosamente")
            return encriptado(nueva_contra)
        

def login(us1, contra1):
    log = False
    while log == False:
        log_us = input("Ingrese su usuario: ")
        log_pasword = input("Ingrese su contraseña: ")
        log_pasword = encriptado(log_pasword)
        if log_us == us1 and log_pasword == contra1:
            print("Inisiaste sesion como:",us1)
            log = True
        else:
            print("Error - Usuario o Contraseña incorrectas")
    print("Bienvenido a Scape The Code")
    

us1 = "pepe"
contra1 = encriptado("pepito123")

login(us1, contra1)
cambiar_contraseña(contra1)