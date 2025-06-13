# Ejercicio 3
# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math

cateto_a = float(input("Ingresa el valor del primer cateto: ")) # Solicitar al usuario el valor del primer cateto

# Solicitar al usuario el valor del segundo cateto
cateto_b = float(input("Ingresa el valor del segundo cateto: "))

# Calcular la hipotenusa usando el teorema de Pitágoras
hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)

# Mostrar el resultado
print("La hipotenusa del triángulo es:", hipotenusa)