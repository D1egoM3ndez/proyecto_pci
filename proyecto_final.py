"""
Proyecto Demo Python
Juego de ahorcado
El programa lanza una palabra secreta y el usuario ingresara
letras para tratar de adivinar la palabra
Al acabar sus intentos, el programa le revela la palabra y le dice si sus intentos fueron correctos o no

"""

"""
Bibliotecas

"""
import random

"""
======================== Función auxiliar =========================

"""

# Lista de palabras para el juego
palabras = ['python', 'programacion', 'juego', 'ahorcado', 'computadora']

# Función para seleccionar una palabra al azar
def seleccionar_palabra(palabras):
    """
        (uso de listas,bibliotecas,funciones)
        De la lista de palabras, la función random
        escoge una palabra para empezar el juego
        Regresa la palabra para empezar a jugar
    """
    return random.choice(palabras)

"""
====================== Función principal del juego===================

"""

def jugar_ahorcado():
    """
        (condicionales, condicionales anidados, ciclos while/for, listas, matrices, strings)
        El programa llama a la función de selección de palabras para empezar a jugar
  
    """
    palabra = seleccionar_palabra(palabras)
    letras_adivinadas = []  # Lista para almacenar las letras que el jugador adivina
    historial_intentos = []  # Lista anidada para registrar los intentos (letra, resultado)
    intentos = 6  # Número de intentos permitidos
    aciertos = 0

    print("¡Bienvenido al juego de ahorcado!")
    print("Tienes", intentos, "intentos para adivinar la palabra.")

    """ Ciclo principal
            Este ciclo es el que nos indica el número total de intentos que tiene
            el usuario para tratar de adivinar la palabra
    """
    
    while intentos > 0:
        
        mostrar_palabra = ''
        
        """
            Ciclo para tratar de adivinar alguna letra
        """
        
        for letra in palabra:
            if letra in letras_adivinadas:
                mostrar_palabra += letra  # Si la letra ha sido adivinada, se muestra
            else:
                mostrar_palabra += '_ '  # Si no, se muestra un guion bajo
        print("\nPalabra:", mostrar_palabra)
        
        if mostrar_palabra.replace(' ', '') == palabra:
            print("\n¡Felicidades, adivinaste la palabra!")
            break
        """
            (uso de variables, strings)
            Se pide una letra en tipo string para comparar el caracter con alguno que este
            en la palabra y pasa esa letra a minúscula, ya que esas son el
            único tipo de letra que hay en las palabras de mi lista
        """
        
        letra = input("Adivina una letra: ").lower()

        """
            (uso de condicionales, condicionales anidados)
            Esta parte nos señala si la letra esta en la palabra oculta o no, o si tarto de poner nuevamente
            una misma letra
        """
        """
            (uso de matrices)
            De igual forma, se usan matrices para llevar el inteto de letra junto
            si es correcto o no a la lista creada en la parte de arriba
        """
        
        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra.")
        elif letra in palabra:
            print("¡Correcto! La letra", letra, "está en la palabra.")
            letras_adivinadas.append(letra)
            historial_intentos.append([letra, "Correcto"])  # Registrar intento como correcto
        else:
            print("Incorrecto. La letra", letra, "no está en la palabra.")
            intentos -= 1
            letras_adivinadas.append(letra)
            historial_intentos.append([letra, "Incorrecto"])  # Registrar intento como incorrecto
            print("Te quedan", intentos, "intentos.")
        
        """
            Situación para cerrar el ciclo
        """
        
        if intentos == 0:
            print("\n¡Lo siento, te has quedado sin intentos!")
            print("La palabra era:", palabra)
    
    """ Mostrar historial de intentos """
    
    print("\nHistorial de intentos:")
    for intento in historial_intentos:
        print("Letra:", intento[0], "- Resultado:", intento[1])

""" Llamada a la función para empezar el juego"""   

# Ejecutar el juego
jugar_ahorcado()