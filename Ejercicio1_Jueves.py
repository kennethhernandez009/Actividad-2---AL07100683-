print ("\nActividad 2 - Ejercicios Jueves Kenneth Hdz")
print ("\nNombre: Kenneth Hernández , Matrícula: AL07100683")

print ("\n=============================================")
print ("Ejercicio 6: Vidas y Daño")
print ("====================BATALLA====================")
#Damos de alta la variable de personaje y vida
personaje = "Lothric"
vida = 100
print (f"\nMi personaje se llama {personaje} y empieza con {vida} de vida")
#Como vida vale 100, esta formula dice: vida = 100 - 25
vida = vida - 25
print  (f"Me dio un golpe de un caballero, ahora tengo vida: {vida}")
#Ahora vida vale 75, esta fórmula dice: vida = 75 - 40
vida = vida - 40 
print (f"Ah, ahora me tocó el golpe de un soldado, tengo de vida {vida}")
# Ahora vida vale 35, esta fórmula dice: vida = 35 - 15
vida = vida - 15
print (f"Me tocó un disparo enemigo!, tengo de vida: {vida}")
#Ahora vida vale 20, esta fórmula dice: vida = 20 + 30
vida = vida + 30
print (f"Tomó una poción..mi vida: {vida}")

print (f"\n{personaje} terminó la batalla con {vida} HP\n")
print ("\n========================================")
