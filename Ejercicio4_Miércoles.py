print ("\nActividad 2 - Ejercicios Miércoles (4) Kenneth Hdz")
print ("\nNombre: Kenneth Hernández , Matrícula: AL07100683")

print ("\n++++++++++++++++++")
print ("Ejercicio realizado por: Kenneth Hernández")
print ("Ejercicio 5: ¿Cuánto dura my playlist?")
print ("\n++++++++++++++++++")

# Duración de cada canción en segundos
canción1 = 204
canción2 = 187
canción3 = 167
canción4 = 184
canción5 = 189

# Sumamos Todo
total_segundos = canción1 + canción2 + canción3 + canción4 + canción5

# Dvisión Entera: Cuántos minutos completos caben
minutos = total_segundos // 60

# % Residuo: Los segundos que sobran
segundos = total_segundos % 60
print ("\nResultados")
print (f"Total en segundos: {total_segundos}")
print (f"Tu playlist dura {minutos} minutos con {segundos} segundos")
print ("\n++++++++++++++++++")
