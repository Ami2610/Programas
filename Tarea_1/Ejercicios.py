# ### Ejercicio 1
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

# print("Hola Mundo")  # Imprime el texto "Hola Mundo"


# ### Ejercicio 2
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
'''
cadena_hola_mundo = "¡Hola Mundo!"  # Guarda el mensaje en una variable
print(cadena_hola_mundo)  # Muestra el contenido de la variable
'''


# ### Ejercicio 3
'''
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por 
pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
'''
'''
nombre_usuario = str(input("Ingrese su nombre: "))  # Pide al usuario que escriba su nombre
print("Hola ", nombre_usuario)  # Saluda al usuario con su nombre
'''


# ### Ejercicio 4
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética.
'''
resultado_operacion = ((3+2) / (2*5)) **2  # Realiza una operación matemática y guarda el resultado
print(resultado_operacion)  # Muestra el resultado de la operación
'''


# ### Ejercicio 5
'''
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.
'''
'''
numero_horas = int(input("Ingrese el número de horas trabajadas: "))  # Pide las horas trabajadas
valor_por_hora = float(input("Ingrese $ por hora: "))  # Pide cuánto se paga por hora
paga_total = numero_horas * valor_por_hora  # Calcula la paga total
print("La paga es: $" + str(paga_total))  # Muestra la paga total
'''


# ### Ejercicio 6
'''
Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en pantalla la suma de todos los
enteros desde 1 hasta n. La suma de los primeros enteros positivos puede ser calculada de la siguiente forma: n*(n + 1)/2
'''
'''
numero = int(input("Ingrese un número entero: "))  # Pide un número entero al usuario
suma = numero*(numero + 1)/2  # Calcula la suma usando la fórmula matemática
print("La suma de los primeros números enteros desde 1 hasta " + str(numero) + " es " + str(suma))  # Muestra la suma
'''


# ### Ejercicio 7
'''
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene 
en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal 
calculado redondeado con dos decimales.
'''
'''
peso = float(input("Ingrese su peso (en kg): "))  # Pide el peso
altura = float(input("Ingrese su altura (en m): "))  # Pide la altura
imc = round((peso / altura ** 2), 2)  # Calcula el IMC y lo redondea a 2 decimales
print("Tu índice de masa corporal es: " + str(imc))  # Muestra el IMC
'''


# ### Ejercicio 8
'''
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r>
donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
'''
'''
n = int(input("Ingrese el número 1 (dividendo): "))  # Pide el dividendo
m = int(input("Ingrese el número 2 (divisor): "))  # Pide el divisor
print(str(n) + " entre " +  str(m) + " da un cociente " + str(n // m) + " y un resto " + str(n % m))  # Muestra cociente y resto
'''


# ### Ejercicio 9
'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el 
capital obtenido en la inversión.
'''

inversion = float(input("Ingrese el valor a invertir: $"))  # Pide la cantidad a invertir
interes_anual = float(input("Ingrese el interés porcentual anual: "))  # Pide el interés anual
años = int(input("Ingrese los años: "))  # Pide la cantidad de años
print("Capital final: $" + str(round(inversion * (interes_anual / 100 + 1) ** años, 2)))  # Calcula y muestra el capital final



# ### Ejercicio 10
'''
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les 
cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada 
payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y 
calcule el peso total del paquete que será enviado.
'''
'''
peso_payaso = 112  # Peso por payaso
peso_muñeca = 75  # Peso por muñeca
payasos = int(input("Ingrese cuantos payasos se enviaran: "))  # Pide cuántos payasos se enviarán
muñecas = int(input("Ingrese cuantas muñecas se enviaran: "))  # Pide cuántas muñecas se enviarán
peso_total = peso_payaso * payasos + peso_muñeca * muñecas  # Calcula el peso total del paquete
print("El peso total del paquete es: " + str(peso_total) + " g")  # Muestra el peso total
'''


# ### Ejercicio 11
'''
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se
cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad 
de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la 
cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
'''
'''
cuenta_ahorros = float(input("Ingrese el valor a depositar: $"))  # Pide el valor inicial del depósito
interes = 0.04  # Tasa de interés del 4%
balance_año1 = cuenta_ahorros * (1 + interes)  # Calcula el saldo tras el primer año
print("El balance después del primer año: $" + str(round(balance_año1, 2)))  # Muestra saldo año 1
balance_año2 = balance_año1 *  (1 + interes)  # Calcula saldo tras segundo año
print("El balance después del segundo año: $" + str(round(balance_año2, 2)))  # Muestra saldo año 2
balance_año3 = balance_año2 * (1 + interes)  # Calcula saldo tras tercer año
print("El balance después del tercer año: $" + str(round(balance_año3, 2)))  # Muestra saldo año 3
'''


# ### Ejercicio 12
'''
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento del 60%. Escribir un programa que comience 
leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el 
descuento que se le hace por no ser fresca y el coste final total.
'''
'''
barras_antiguas = int(input("Ingrese la cantidad de barras de pan antiguas vendidas: "))  # Pide la cantidad de barras no frescas
precio_habitual = 3.49  # Precio normal de una barra
descuento = 0.60  # Descuento del 60%
descuento_por_barra = precio_habitual * descuento  # Calcula el descuento por barra
precio_descuento = barras_antiguas * precio_habitual * (1 - descuento)  # Precio final con descuento
print("Precio habitual de la barra de pan: $" + str(precio_habitual))  # Muestra el precio normal
print("Descuento por barra: $" + str(round(descuento_por_barra, 2)))  # Muestra el descuento
print("Precio final: $" + str(round(precio_descuento, 2)))  # Muestra el precio final
'''
