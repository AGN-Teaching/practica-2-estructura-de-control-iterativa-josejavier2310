# Plant
# Introduccion
print("Practica 2")
print("Estructura de control Iterativa")
print("Jose Javier Perez Ledesma")
print("codigo desifrar.py")
# Algoritmo
def descifrar_mensaje(mensaje_cifrado):
    # Extraer k a partir de las dos primeras letras del mensaje cifrado
    primera_letra = ord(mensaje_cifrado[0]) - 65
    segunda_letra = (ord(mensaje_cifrado[1]) - 65) // 2
    k = primera_letra if primera_letra == segunda_letra else (primera_letra + segunda_letra) // 2
    mensaje_descifrado = ""
    for caracter in mensaje_cifrado[2:]:  # Omitir los dos primeros caracteres
        if caracter.isalpha():
            ascii_offset = 65 if caracter.isupper() else 97
            nuevo_caracter = chr((ord(caracter) - ascii_offset - k) % 26 + ascii_offset)
            mensaje_descifrado += nuevo_caracter
        else:
            mensaje_descifrado += caracter
    return mensaje_descifrado, k
# Entrada del usuario
mensaje_cifrado = input("Introduce el mensaje cifrado: ")
mensaje_descifrado, k = descifrar_mensaje(mensaje_cifrado)
print("\nMensaje descifrado:", mensaje_descifrado)
print("Clave de cifrado detectada:", k)illa descifrar.py
