print ("\nActividad 2 - Ejercicios Jueves (3) Kenneth Hdz")
print ("\nNombre: Kenneth Hernández , Matrícula: AL07100683")

print ("\n*****************************************************")
print ("Ejercicio 8: Mi Tiempo de Pantalla")
print ("******************TIEMPO DE PANTALLA*******************")
#Damos de alta la variable app y las horas que paso al día
app = "Instagram"
horas_diarias = 2
print (f"\nPaso {horas_diarias} horas diarias en {app}")

#Calculamos las horas al año, esta fórmula dice: horas_anio = 2 * 365
horas_anio = horas_diarias * 365
print (f"Al año son {horas_anio} horas")

#Convertimos las horas a días completos (1 Día tiene 24 horas)
#Esta fórmula dice: días_anio = 730 / 24, que da 30.41666
días_anio = horas_anio / 24
#El :.1f muestra solo 1 decimal, así que se ve 30.4
print (f"¡Eso equivale a {días_anio:.1f} días completos sin parar!")

#Calculamos cuántos meses son (un mes tiene aprox. 30 días)
#Esta fórmula dice: meses = 30.4 / 30
meses = días_anio / 30
print (f"\nO sea, casi {meses:.1f} meses de mi año se van en {app}\n")
print ("\n*****************************************************")
