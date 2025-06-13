# Ejercicio 14
# Invertir un número de dos cifras (por ejemplo: 23 → 32).

# Pedir al usuario un número de dos cifras
numero = int(input("Ingresa un número de dos cifras: "))

# Separar las decenas y las unidades
decenas = numero // 10
unidades = numero % 10

# Invertir las cifras
numero_invertido = unidades * 10 + decenas

# Mostrar el resultado
print(f"Número invertido: {numero_invertido}")