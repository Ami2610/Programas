# Ejercicio 14
# El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno
# y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o 
# más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si
# son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. Realice un 
# algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.

# Se pide la cantidad de alumnos
cantidad_alumnos = int(input("Introduce la cantidad de alumnos: "))

# Se determina el costo por alumno según la cantidad
if cantidad_alumnos >= 100:
    costo_por_alumno = 65
elif cantidad_alumnos >= 50:
    costo_por_alumno = 70
elif cantidad_alumnos >= 30:
    costo_por_alumno = 95
else:
    # Si son menos de 30, el costo total es fijo
    costo_por_alumno = 4000 / cantidad_alumnos

# Se calcula el costo total
costo_total = costo_por_alumno * cantidad_alumnos

# Se muestran los resultados
print("Cada alumno debe pagar: {:.2f} euros".format(costo_por_alumno))
print("Costo total del viaje: {:.2f} euros".format(costo_total))
