#Cuando termine el tema de if-else, agregare en esta parte una restricción de edad
def posibilidad_de_jugar (edad):
edad = int(input("Hola y bienvenid@ a esta aventura, para inciar por favor, introduce tu edad:"))

# Pokemon que puedan aparacer como enemigos:

pok1 = 160
pok2 = 200
pok3 = 250

# Ataques que como usuario podran utilizar

atq1 = 75
atq2 = 120
atq3 = 160
atq4 = 190
atq5 = 230

# Diferentes escenarios
# Ya visto el tema de funciones, creo que lo mejor sería que cada partida este guardada en una,
# para que cuando este haciendo los ciclos, pueda llamar a esas funciones para que sea más facil el proceso

def par1(pok1,atq1):
    jug1= pok1 - atq1
return jug1

def par2 (pok1,atq2):
    jug2= pok1 - atq2
return jug2

def par3 (pok1,atq3):
    jug3= pok1 - atq3
return jug3

def par4 (pok1,atq4):
    jug4= pok1 - atq4
return jug4

def par5 (pok1,atq5):
    jug5= pok1 - atq5
return jug5

def par6 (pok2,atq1):
    jug6= pok2 - atq1
return jug6

def par7 (pok2,atq2):
    jug7= pok2 - atq2
return jug7

def par8 (pok2,atq3):
    jug8= pok2 - atq3
return jug8

def par9 (pok2,at4):
    jug9= pok2 - atq4
return jug9

def par10 (pok2,atq5):
    jug10= pok2 - atq5
return jug10

def par11 (pok3, atq1):
    jug11= pok3 - atq1
return jug11

def par12 (pok3,atq2):
    jug12= pok3 - atq2
return jug12

def par13 (pok3,atq3):
    jug13= pok3 - atq3
return jug13

def par14 (pok3,atq4):
    jug14= pok3 - atq4
return jug14

def par15 (pok5,atq3):
    jug15= pok3 - atq5
return jug15

#Para este caso, cuando conoscamos más sobre if-else, cuando el ataque sea mayor al valor de vida de cada objetivo se ira
#avanzando en la aventura enfrentandote a cada enemigo cada vez más dificil
#Ejemplo:

if jug1 > pok1:
    print ("Ganaste, sigue avanzando")
    print ("Un nuevo enemigo se acerca")
    
else:
    print("Game over")



