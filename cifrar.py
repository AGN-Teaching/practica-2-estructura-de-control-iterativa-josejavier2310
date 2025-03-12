# Plantilla cifrar.py
# Introduccion
print("Practica 2")
print("Estructura de control iterartiva")
print("Jose Javier Perez Ledesma")
print("Codigo cifrar.py")
# Algoritmo
import random
def cifrar_mensaje(mensaje, k):
    mensaje_cifrado = ""
    for caracter in mensaje:
        if caracter.isalpha():
            ascii_offset = 65 if caracter.isupper() else 97
            nuevo_caracter = chr((ord(caracter) - ascii_offset + k) % 26 + ascii_offset)
            mensaje_cifrado += nuevo_caracter
        else:
            mensaje_cifrado += caracter
    # Estrategia creativa: ocultar k en las primeras dos letras del mensaje
    ocultar_k = chr( 65 + (k % 26)) + chr(65 + ((k * 2) % 26))
    return ocultar_k + mensaje_cifrado, k
# Entrada del usuario
mensaje_original = input("Introduce el mensaje a cifrar: ")
k = random.randint(3, 15) # Generar k aleatorio
mensaje_cifrado, k = cifrar_mensaje(mensaje_original, k)
print("\nMensaje cifrado:", mensaje_cifrado)
print("Clave de cifrado:", k)
