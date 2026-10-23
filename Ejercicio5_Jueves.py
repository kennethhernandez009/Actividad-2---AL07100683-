print ("\nActividad 2 - Ejercicios Jueves (5) Kenneth Hdz")
print ("\nNombre: Kenneth Hernández , Matrícula: AL07100683")

print ("\n****************************************************")
print ("Ejercicio 10: Reto Final, ¿Soy Viral?")
print ("CALCULADORA DE ENGAGEMENT HECHA POR KENNETH")

#input() guarda texto, aquí no convertirmos porque el usuario es texto
#Si el usuario escribe mi_cuenta, ahora usuario vale "mi_cuenta"
usuario = input("\nTu usuario de Instagram / TikTok: @")

#int() convierte el texto a número entero para poder hacer cuentas
#Si el usuario escribe 700, ahora seguidores vale 700
seguidores = int(input("¿Cuántos seguidores tienes?"))
#Si el usuario escribe 64, ahora likes vale 64
likes = int(input("¿Cuántos likes tuvo tu último post?"))
#Si el usuario escribe 21, ahora comentarios vale 21
comentarios = int(input("¿Cuántos comentarios tuvo?"))

#Sumamos todas las interacciones, esta formula dice 64 + 21
#Ahora interacciones vale 85
interacciones = likes * comentarios

#Calculamos el engagement: qué porcentaje de mis seguidores interactuó
#Los paréntesis hacen que la división se haga ANTES de multiplicar por 100
#Esta fórmula dice: engagement = (85/700) * 100, o sea 0.12 * 100
engagement = (interacciones/seguidores) * 100
#Ahora engagement vale 12.0

print (f"\n***************RESULTADOS DE @{usuario}******************")
print (f"Interacciones totales: {interacciones}")
#El :.2f muestra 2 decimales, así que se ve 12.00%
print (f"Engagement: {engagement:.2f}%")
print ("\nDato: En redes, un engagement arriba de 3% ya se considera bueno")
print ("\n******************************************************************")

