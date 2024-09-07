import random
# Lista de palabras para el juego palabras = ['python', 'programacion', 'juego', 'ahorcado', 'computadora']
# Función para seleccionar una palabra al azar
def seleccionar_palabra(palabras):
    return random.choice(palabras)
# Función principal del juego
def jugar_ahorcado():
    palabra = seleccionar_palabra(palabras)
    letras_adivinadas = []
# Lista para almacenar las letras que el jugador adivina

intentos = 6  # Número de intentos
permitidos aciertos = 0

print("¡Bienvenido al juego de ahorcado!")
print("Tienes", intentos, "intentos para adivinar la palabra.")

if letra in letras_adivinadas:
    mostrar_palabra += letra
# Si la letra ha sido adivinada, se muestra
else: mostrar_palabra += '_ '
# Si no, se muestra un guion bajo

print("\nPalabra:", mostrar_palabra)

if mostrar_palabra.replace(' ', '') == palabra:
    print("\n¡Felicidades, adivinaste la palabra!")
   
letra = input("Adivina una letra: ").lower()

if letra in letras_adivinadas:
    print("Ya adivinaste esa letra.")

elif letra in palabra:
    print("¡Correcto! La letra", letra, "está en la palabra.")
    letras_adivinadas.append(letra)

else:
    print("Incorrecto. La letra", letra, "no está en la palabra.")
    intentos -= 1 letras_adivinadas.append(letra)
    print("Te quedan", intentos, "intentos.")
        if intentos == 0:
            print("\n¡Lo siento, te has quedado sin intentos!")
            print("La palabra era:", palabra)
# Ejecutar el juego
jugar_ahorcado()