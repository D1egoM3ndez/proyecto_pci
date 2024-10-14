# proyecto_pci
proyecto 1 de pci

# PROYECTO "JUEGO DE AHORCADO"

Los videojuegos son algo común en el día a día, según una encuesta realizada por el Statista Research Department: "Entre una y cinco horas semanales es la frecuencia más popular para jugar videojuegos entre los mexicanos. Aproximadamente 35% de los encuestados dijeron jugar en este periodo de tiempo. En el otro extremo, únicamente un 3% juega más de 20 horas semanales." (https://es.statista.com/estadisticas/1301324/frecuencia-semanal-de-uso-de-videojuegos-en-mexico/); esto ralizado en México en el año en curso.
No es de sorprenderse que varios jóvenes pasan sus ratos libres frente a una pantalla, gracias a que la tecnología a ayudado a que cada vez se vuelvan más impresionantes las cosas que podemos ver en una pantalla.

Para mi proyecto pensé en uno de los juegos más comunes para comenzar desde lo más básico, para entender como va a funcionar esto, será de la siguiente manera:
1.- Aparecera una palabra incompleta
2.- El usuario ingresara letras para tratar de adivinar la palabra
3.- El programa le dira si esa letra esta o no en la palabra 
4.- Contara con cierto número de intentos para adivinar, si no lo logra perderá y ahi acabara el programa

Para este proyecto lo cambié en su momento por que me parecía que el otro era un poco más complicado para los conocimientos que tenía

======================= Sub-competencia 1 =======================================
Sub-competencia: 
  Separa el código en funciones pequeñas reusables, haciendo uso correcto de paso por parametros y return (avance 3)
Error: 
  La segunda función no estaba bien tabulada y no corría el programa, además, en la segunda estaba mal llamada la primera función

Tabulación:
  def jugar_ahorcado():
  palabra = seleccionar_palabra(palabras)
  letras_adivinadas = []  # Lista para almacenar las letras que el jugador adivina
  historial_intentos = []  # Lista anidada para registrar los intentos (letra, resultado)
  intentos = 6  # Número de intentos permitidos
  aciertos = 0

  print("¡Bienvenido al juego de ahorcado!")
  print("Tienes", intentos, "intentos para adivinar la palabra.")

Llamada de la función:
  def jugar_ahorcado():
  palabra = def (seleccionar_palabra(palabras))
    
Cambio realizado: Tabule todas las funciones correctamente, además de corregir las llamadas a la función que estaban erróneas

Tabulación:
  
  def jugar_ahorcado():
    palabra = seleccionar_palabra(palabras)
    letras_adivinadas = []  # Lista para almacenar las letras que el jugador adivina
    historial_intentos = []  # Lista anidada para registrar los intentos (letra, resultado)
    intentos = 6  # Número de intentos permitidos
    aciertos = 0

    print("¡Bienvenido al juego de ahorcado!")
    print("Tienes", intentos, "intentos para adivinar la palabra.")

Llamada de la función:

  def jugar_ahorcado():
    palabra = seleccionar_palabra(palabras)
    
Lineas: 83 = Corrección de la llamada de la función
        83 a 89 = Nueva tabulación

======================== Sub-competencia 2 ======================================
Sub-competencia: 
  Aplica estructuras condicionales para resolver un problema (avance 4)

Error: Como todavía no había agregado ciclos while o for hasta ese momento el código no corría, entonces la variable que medía los intentos para adivinar marcaba un error, gracias a que el ciclo la declaraba.

Cambio realizado: Después de terminar ciclos while, agregue el ciclo donde pertenecía al inicio para ahora si que corriera el programa
  
   while intentos > 0:
        mostrar_palabra = ''
        for letra in palabra:
            if letra in letras_adivinadas:
                mostrar_palabra += letra  # Si la letra ha sido adivinada, se muestra
            else:
                mostrar_palabra += '_ '  # Si no, se muestra un guion bajo

Lineas: 92 y 96 = ciclos agregados

======================== REFERENCIAS ======================================
Para este programa fue requerido el uso de la biblioteca random(), junto con la funcion de secuencia .choice(), adquiriendo esto de:
https://docs.python.org/3/library/random.html
