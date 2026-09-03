print("Bienvenido a Scape The Code")

def encriptado(contra):
    resultado = ""
    for caracter in contra:
        codigo= ord(caracter)
        n_cod = codigo + 4
        resultado += chr(n_cod)
    return resultado
        
def login(usuario,contra):
    log = False
    while log == False:
        log_us = input("Ingrese su usuario: ")
        log_pasword = input("Ingrese su contraseña: ")
        log_pasword = encriptado(log_pasword)
        if log_us == usuario and log_pasword == contra:
            print("Inisiaste sesion como:",usuario)
            log = True
        else:
            print("Error - Usuario o Contraseña incorrectas")
    return log

us1 = "pepe"
contra1 = encriptado("pepito123")
print(contra1)

log = login(us1, contra1)