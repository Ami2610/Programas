# Ejercicio 18
# Haz un programa que muestre un cronómetro, indicando horas, minutos y segundos.

import time  # Importamos la librería para controlar el tiempo

# Definimos el tiempo inicial del cronómetro
horas = 0
minutos = 0
segundos = 0

print("Cronómetro iniciado (presiona Ctrl + C para detenerlo):\n")

try:
    # Bucle infinito que cuenta el tiempo
    while True:
        # Mostramos el tiempo actual con formato 00:00:00
        print(f"{horas:02d}:{minutos:02d}:{segundos:02d}", end="\r")
        time.sleep(1)  # Espera 1 segundo

        # Incrementamos el tiempo
        segundos += 1
        if segundos == 60:
            segundos = 0
            minutos += 1
        if minutos == 60:
            minutos = 0
            horas += 1
except KeyboardInterrupt:
    # Finaliza el cronómetro cuando el usuario lo detiene con Ctrl+C
    print(f"\nCronómetro detenido en: {horas:02d}:{minutos:02d}:{segundos:02d}")
