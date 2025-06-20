# Ejercicio 8
# Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la nota es mayor 
# o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo 
# sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.

# Se pide la nota del estudiante
nota = float(input("Introduce la nota: "))

# Se pide la edad del estudiante
edad = int(input("Introduce la edad: "))

# Se pide el sexo del estudiante (F o M)
sexo = input("Introduce el sexo (F/M): ").upper()

# Se evalúan las condiciones de aceptación
if nota >= 5 and edad >= 18:
    if sexo == 'F':
        print("ACEPTADA")
    elif sexo == 'M':
        print("POSIBLE")
    else:
        print("NO ACEPTADA")
else:
    print("NO ACEPTADA")
