"""
Proyecto python
Simulador de juego ahorcado
El programa genera una palabra secreta, la cual el usuario intentará
adivinar introduciendo letras que piense queestan en la palabra.
Al final de sus intentos se revela la palabra y le genera el historial
de sus intentos
"""

"""
Bibliotecas utilizadas

"""
import random

"""
Listas utilizadas

"""
# Definimos el alfabeto como un string
alfabeto = "abcdefghijklmnopqrstuvwxyz"

# Lista de palabras para el juego
palabras = ['python', 'programacion', 'juego', 'ahorcado', 'computadora']

"""
======================= Funciones auxiliares ============================

"""
def seleccionar_palabra(palabras):
    
    """
    (uso de funciones y listas)
    Recibe: Lista de palabras de la parte superior
    Selecciona una palabra al azar de la lista proporcionada para empezar
    a jugar
    Devuelve: Palabra para jugar
    
    """
    return random.choice(palabras)

def validar_letra(letra):
    
    """
    (uso de funciones, strings)
    Recibe: Letra introducida por el usuario
    Valida que la entrada del usuario sea una sola letra de la lista
    del alfabeto de la parte de arriba y que sea solo 1 letra a la vez
    Devuelve: Operador True o False
    
    """
    return len(letra) == 1 and letra in alfabeto

def mostrar_historial(historial):
    
    """
    (uso de funciones, matrices, ciclos for)
    Recibe: Lista anidada donde estan guardados los intentos del usuario
    junto con si es correcto o incorrecto
    Muestra el historial de intentos del usuario al adivinar alguna letra
    Devuelve: Historial de intentos
    
    """
    print("\nHistorial de intentos:")
    for intento in historial:
        print(f"Letra: {intento[0]} - Resultado: {intento[1]}")

"""

========================= Función principal ===============================

"""

def jugar_ahorcado():
    
    """
    (uso de ciclos, ciclos anidados, condicionales, variables, 
    matrices, listas)
    Función principal que ejecuta el juego del ahorcado.
    Devuelve: Llama a las anteriores funciones para empezar a jugar
    
    """
    palabra = seleccionar_palabra(palabras)
    letras_adivinadas = []  # Lista para almacenar las letras adivinadas
    historial_intentos = []  # Lista para almacenar el historial de intentos
    intentos = 6  # Número de intentos permitidos

    print("¡Bienvenido al juego de ahorcado!")
    print("Tienes", intentos, "intentos para adivinar la palabra.")

    #ciclo principal
    while intentos > 0:
        mostrar_palabra = ''
        
        # Mostrar la palabra con letras adivinadas
        for letra in palabra:
            if letra in letras_adivinadas:
                mostrar_palabra += letra + ' '  
                # Si la letra ha sido adivinada, se muestra
            else:
                mostrar_palabra += '_ '  # Si no, se muestra un guion bajo
        print("\nPalabra:", mostrar_palabra.strip())
        
        if mostrar_palabra.replace(' ', '') == palabra:
            print("\n¡Felicidades, adivinaste la palabra!")
            break
        
        letra = input("Adivina una letra: ").lower()

        # Validar la letra ingresada
        if not validar_letra(letra):
            print("Entrada no válida. Ingresa solo una letra del alfabeto.")
            continue
        
        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra.")
        elif letra in palabra:
            print("¡Correcto! La letra", letra, "está en la palabra.")
            letras_adivinadas.append(letra)
            #Registrar intento como correcto
            historial_intentos.append([letra, "Correcto"]) 
        else:
            print("Incorrecto. La letra", letra, "no está en la palabra.")
            intentos -= 1
            letras_adivinadas.append(letra)
            #Registrar intento como incorrecto
            historial_intentos.append([letra, "Incorrecto"]) 
            print("Te quedan", intentos, "intentos.")
        
        # Situación para cerrar el ciclo
        if intentos == 0:
            print("\n¡Lo siento, te has quedado sin intentos!")
            print("La palabra era:", palabra)

    # Mostrar historial de intentos
    mostrar_historial(historial_intentos)

# Ejecutar el juego
jugar_ahorcado()
