
# CIFRADO VERNAM
# Alfabeto de 27 caracteres
# A=0, B=1, ..., Z=25, espacio=26

MODULO = 27

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "


# Funcion para convertir texto a numeros
def convertir_a_numeros(texto):

    numeros = []

    texto = texto.upper()

    for caracter in texto:

        if caracter in ALFABETO:
            numeros.append(ALFABETO.index(caracter))

        else:
            print("Caracter no valido:", caracter)
            return None

    return numeros


# Funcion para convertir numeros a texto
def convertir_a_texto(numeros):

    texto = ""

    for numero in numeros:
        texto += ALFABETO[numero % MODULO]

    return texto


# Funcion para cifrar
def cifrar(mensaje, clave):

    mensaje_numeros = convertir_a_numeros(mensaje)
    clave_numeros = convertir_a_numeros(clave)

    if mensaje_numeros is None or clave_numeros is None:
        return None

    # La clave debe tener la misma longitud
    if len(mensaje_numeros) != len(clave_numeros):

        print("Error: la clave debe tener la misma longitud")
        print("que el mensaje.")

        return None

    resultado = []

    # Cifrado: C = (P + K) mod 27
    for i in range(len(mensaje_numeros)):

        valor = (
            mensaje_numeros[i] + clave_numeros[i]
        ) % MODULO

        resultado.append(valor)

    return convertir_a_texto(resultado)


# Funcion para descifrar
def descifrar(mensaje_cifrado, clave):

    cifrado_numeros = convertir_a_numeros(mensaje_cifrado)
    clave_numeros = convertir_a_numeros(clave)

    if cifrado_numeros is None or clave_numeros is None:
        return None

    # La clave debe tener la misma longitud
    if len(cifrado_numeros) != len(clave_numeros):

        print("Error: la clave debe tener la misma longitud")
        print("que el mensaje cifrado.")

        return None

    resultado = []

    # Descifrado: P = (C - K) mod 27
    for i in range(len(cifrado_numeros)):

        valor = (
            cifrado_numeros[i] - clave_numeros[i]
        ) % MODULO

        resultado.append(valor)

    return convertir_a_texto(resultado)


# MENU PRINCIPAL
while True:

    print("\n===== CIFRADO VERNAM =====")
    print("1. Cifrar")
    print("2. Descifrar")
    print("3. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":

        mensaje = input("Escribe el mensaje: ")
        clave = input("Escribe la clave: ")

        resultado = cifrar(mensaje, clave)

        if resultado is not None:
            print("Mensaje cifrado:", resultado)

    elif opcion == "2":

        mensaje = input("Escribe el mensaje cifrado: ")
        clave = input("Escribe la clave: ")

        resultado = descifrar(mensaje, clave)

        if resultado is not None:
            print("Mensaje descifrado:", resultado)

    elif opcion == "3":

        print("Programa terminado.")
        break

    else:

        print("Opcion no valida.")