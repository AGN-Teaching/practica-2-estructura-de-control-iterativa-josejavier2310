# Introduccion
print("Practica 2")
print("Estructura de control iterartiva")
print("Jose Javier Perez Ledesma")
print("Codigo cifrar.py")
# Algoritmo
import random # Importamos random para generar un numero aleatorio
def cifrar_mensaje(mensaje, k): # Resive un mensaje y numero de desplazamiento 
    mensaje_cifrado = "" # Inicializamos una cadena vacia para almacenar el mensaje cifrado
    for caracter in mensaje:
        if caracter.isalpha(): # Si es una letra
            ascii_offset = 65 if caracter.isupper() else 97 # Determina si es mayuscula
            nuevo_caracter = chr((ord(caracter) - ascii_offset + k) % 26 + ascii_offset) # Formula del cifrado
            mensaje_cifrado += nuevo_caracter
        else:
            mensaje_cifrado += caracter
    # Estrategia creativa: ocultar k en las primeras dos letras del mensaje
    ocultar_k = chr( 65 + (k % 26)) + chr(65 + ((k * 2) % 26)) # Covierte k en letra
    return ocultar_k + mensaje_cifrado, k # Es una variacion de k
# Entrada del usuario
mensaje_original = input("Introduce el mensaje a cifrar: ") # Solicitamos el mensaje 
k = random.randint(3, 15) # Generar k aleatorio
mensaje_cifrado, k = cifrar_mensaje(mensaje_original, k)
print("\nMensaje cifrado:", mensaje_cifrado)# Cifra el mensaje
print("Clave de cifrado:", k) # Imprime el mensaje
