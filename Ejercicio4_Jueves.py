print ("\nActividad 2 - Ejercicios Jueves (4) Kenneth Hdz")
print ("\nNombre: Kenneth Hernández , Matrícula: AL07100683")

print ("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print ("Ejercicio 9: Tienda de Mascotas Interactiva")
print ("Tienda de Mascotas de Kenneth")
#input() le pregunta al usuario y guarda lo que escribe en la variable
#input() SIEMPRE guarda TEXTO, aunque escribas un número
mascota = input ("\n¿Qué mascota quieres adoptar?")
#Si el usuario escribe perro, ahora mascota vale "perro"

#float() convierte el texto a número con decimales para poder hacer cuentas
precio_mascota = float(input(f"¿Cuánto cuesta el/la {mascota}?$"))
#Si el usuario escribe 1800, ahora precio_mascota vale 1800.0
precio_croquetas = float (input("¿Cuánto cuesta un mes de croquetas/alimento? $"))
#Si el usuario escribe 280, ahora el precio_croquetas vale 280.0
#int() convierte el texto a número entero, porque los meses no llevan decimales
meses = int(input("¿Para cuántos meses quieres croquetas/alimento?"))
#Si el usuario escribe 5, ahora meses vale 5

#Cálculamos cuánto gasto en croquetas, esta fórmula dice: costo_croquetas = 280.0 * 5
costo_croquetas = precio_croquetas * meses
#Ahora costo_croquetas valdría 1400.0

#Calculamos el total, esta fórmula dice: total = 1800.0 + 1400.0
total = precio_mascota + costo_croquetas
#Ahora total vale 3200.0

print ("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print ("Ticket de Compra")
#El :.2f muestra 2 decimales, como se de el dinero
print (f"Mascota: {mascota} ${precio_mascota:.2f}")
print (f"\nTOTAL A PAGAR: ${total:.2f}\n")
print ("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


