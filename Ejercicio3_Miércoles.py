print ("\nActividad 2 - Ejercicios Miércoles (3) Kenneth Hdz")
print ("\nNombre: Kenneth Hernández , Matrícula: AL07100683")

print ("\n❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤")
print ("Ejercicio realizado por: Kenneth Hernández")
print ("Ejercicio 4: ¿Cuánto tardo en terminar una seríe?")
print ("\n❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤")

# Damos de alta las variables
serie = "Dexter"
temporadas = 8
episodios_por_temporada = 12
minutos_por_episodio = 50 
horas_al_día = 2 # Cuánto tiempo le dedico a diario
# Usamos las variables en las fórmulas
# Total de episodios
total_episodios = temporadas * episodios_por_temporada

# Total de minutos y horas

total_minutos = total_episodios * minutos_por_episodio
total_horas = total_minutos / 60 

# ¿Cuántos días necesito?
días_necesarios = total_horas / horas_al_día

print ("\nResultados")
print (f"{serie} tiene {total_episodios} episodios")
print (f"Son {total_minutos} minutos en total")
print (f"Equivale a {total_horas:.1f} horas")
print (f"Viendo {horas_al_día} horas diarias, la terminas en {días_necesarios:.1f} días")
print ("\n❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤")