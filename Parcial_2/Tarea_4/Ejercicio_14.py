# Ejercicio 14
# Una persona está en el km 70 de una carretera, y otra en el km 150. Los coches van en sentido opuesto con la misma velocidad. 
# Realiza un programa para determinar en qué kilómetro se encontrarán.

# Posiciones iniciales
pos_persona1 = 70
pos_persona2 = 150

# Suponemos que ambos coches se mueven hacia el centro con la misma velocidad
# Esto significa que se acercan a la misma velocidad por igual desde ambos extremos

# La distancia total entre ellos
distancia_total = pos_persona2 - pos_persona1  # 150 - 70 = 80 km

# Como ambos se mueven a la misma velocidad y en sentido opuesto, se encontrarán en el punto medio
punto_encuentro = pos_persona1 + (distancia_total / 2)

# Mostramos el resultado
print(f"Los coches se encontrarán en el kilómetro {punto_encuentro}")
