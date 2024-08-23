edad = int(input("Hola y bienvenid@ a esta aventura, para inciar por favor, introduce tu edad:"))
# Cuando veamos el tema de if-else, se pondra una restricción de edad para que mayores a 15 años solo puedan jugar
# De igual forma, para más adelante haremos todas las siguientes operaciones de manera de juego y aleatoriamente

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

jug1= pok1 - atq1
jug2= pok1 - atq2
jug3= pok1 - atq3
jug4= pok1 - atq4
jug5= pok1 - atq5

jug6= pok2 - atq1
jug7= pok2 - atq2
jug8= pok2 - atq3
jug9= pok2 - atq4
jug10= pok2 - atq5

jug11= pok3 - atq1
jug12= pok3 - atq2
jug13= pok3 - atq3
jug14= pok3 - atq4
jug15= pok3 - atq5

#Para este caso, cuando conoscamos más sobre if-else, cuando el ataque sea mayor al valor de vida de cada objetivo se ira
#avanzando en la aventura enfrentandote a cada enemigo cada vez más dificil
#Ejemplo:

if jug1 > pok1:
    print ("Ganaste, sigue avanzando")
    print ("Un nuevo enemigo se acerca")
    
else:
    print("Game over")



