print("Bienvenido a Scape The Code")

def login(usuario,contra):
    log = False
    while log == False:
        log_us = input("Ingrese su usuario: ")
        log_pasword = input("Ingrese su contraseña: ")
        if log_us == usuario and log_pasword == contra:
            print("Inisiaste sesion como:",usuario)
            log = True
        else:
            print("Error - Usuario o Contraseña incorrectas")

    return log

log = login("pepe","wzq")