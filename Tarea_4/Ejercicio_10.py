# Ejercicio 10
# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. 
# El programa debe determinar qué tipo de triangulo es, teniendo en cuenta los siguiente:
    # Si se cumple Pitágoras entonces es triángulo rectángulo.
    # Si sólo dos lados del triángulo son iguales entonces es isósceles.
    # Si los 3 lados son iguales entonces es equilátero.
    # Si no se cumple ninguna de las condiciones anteriores, es escaleno.

# Se ingresan los tres lados del triángulo
lado_a = float(input("Introduce el lado A: "))
lado_b = float(input("Introduce el lado B: "))
lado_c = float(input("Introduce el lado C: "))

# Verificamos si todos los lados son iguales
if lado_a == lado_b == lado_c:
    print("Es un triángulo equilátero.")
# Verificamos si solo dos lados son iguales
elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
    print("Es un triángulo isósceles.")
# Verificamos si cumple con el teorema de Pitágoras para triángulo rectángulo
elif (pow(lado_a, 2) + pow(lado_b, 2) == pow(lado_c, 2)) or \
     (pow(lado_a, 2) + pow(lado_c, 2) == pow(lado_b, 2)) or \
     (pow(lado_b, 2) + pow(lado_c, 2) == pow(lado_a, 2)):
    print("Es un triángulo rectángulo.")
# Si no cumple ninguna de las condiciones anteriores
else:
    print("Es un triángulo escaleno.")
