print ("\nActividad 2 - Ejercicios Miércoles (2) Kenneth Hdz")
print ("\nNombre: Kenneth Hernández , Matrícula: AL07100683")

print ("******************************")
print ("\nEjercicio 3: ¿Cuánto escucho a mi artista favorito?")
print ("\nMI ARTISTA FAVORITO\n")

artista = "DPR IAN"
canciones_por_día = 4
duración_promedio = 3.25 # minutos por canción

minutos_día = canciones_por_día *  duración_promedio
minutos_anio = minutos_día * 365 
horas_anio = minutos_anio / 60
días_anio = horas_anio / 24

print (f"Escuchas a {artista} {minutos_día} minutos al día")
print (f"Al año son {minutos_anio} minutos")
print (f"Eso equivale a {horas_anio:.1f} horas")
print (f"O sea {días_anio:.1f} días completos escuchando a {artista}!\n")
