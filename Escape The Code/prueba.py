import re

def encriptado(contra):
    resultado = ""
    for caracter in contra:
        codigo= ord(caracter)
        n_cod = codigo + 4
        resultado += chr(n_cod)
    return resultado

def cambiar_contraseña(contra1):
    log_pasword = input("Ingrese su contraseña actual: ")
    log_pasword = encriptado(log_pasword)
    if log_pasword == contra1:
        nueva_contra = input("Ingrese su nueva contraseña: ")
        nueva_contra = encriptado(nueva_contra)
        print("Contraseña cambiada exitosamente")
        return nueva_contra
    else:
        print("Error - Contraseña incorrecta")

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