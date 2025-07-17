# Ejercicio 5
# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica 
# “Has entrado al sistema”, sino se da un error.

# Solicitamos el nombre de usuario
usuario = input("Introduce el nombre de usuario: ")

# Solicitamos la contraseña
contrasena = input("Introduce la contraseña: ")

# Verificamos si ambos datos coinciden con los requeridos
if usuario == "pepe" and contrasena == "asdasd":
    print("Has entrado al sistema.")
else:
    # Si no coinciden, mostramos error
    print("Error en el usuario o la contraseña.")
