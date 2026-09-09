from salas.Ahorcado import jugar_ahorcado, palabras
from salas.Batalla_Naval import mini_batalla_naval

print("Bienvenido a Scape The Code")

def encriptado(contra):
    resultado = ""
    for caracter in contra:
        codigo= ord(caracter)
        n_cod = codigo + 4
        resultado += chr(n_cod)
    return resultado

def menu():
    print("0. Instrucciones")
    print("1. Jugar")
    print("2. Cambiar Contraseña")
    print("3. Cerrar Sesión")
    input_usuario = input("Ingrese una opción: ")
    if input_usuario.isdigit():
        input_usuario = int(input_usuario)
        if input_usuario == 0:
            print("\nBienvenido a Scape The Code. En este juego, deberás superar dos salas para ganar. La primera sala es un juego de Ahorcado, donde tendrás que adivinar la palabra correcta antes de quedarte sin intentos. La segunda sala es un juego de Batalla Naval, donde deberás hundir todos los barcos enemigos antes de quedarte sin disparos. ¡Buena suerte!")
            print("\n")
            menu()
        elif input_usuario == 1:
            sala_1=jugar_ahorcado()
            if sala_1==True:
                sala_2=mini_batalla_naval()
        elif input_usuario == 2:
            cambiar_contraseña(contra1)
        elif input_usuario == 3:
            print("Cerrando sesión...")
            login(us1, contra1)
        else:
            print("Error - Ingrese un número válido")
            menu()
    else:
        print("Error - Ingrese un número")
        menu()

def cambiar_contraseña(contra1):
    log_pasword = input("Ingrese su contraseña actual: ")
    log_pasword = encriptado(log_pasword)
    if log_pasword == contra1:
        nueva_contra = input("Ingrese su nueva contraseña: ")
        nueva_contra = encriptado(nueva_contra)
        print("Contraseña cambiada exitosamente")
        menu()
    else:
        print("Error - Contraseña incorrecta")
        menu()

    

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
    menu()

us1 = "pepe"
contra1 = encriptado("pepito123")

login(us1, contra1)