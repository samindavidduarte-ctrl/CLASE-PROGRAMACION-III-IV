# Verificación si una contraseña coincide con una predefinida

# Contraseña guardada en el sistema Previamente
contrasena_correcta = "Duarte1996"

# Solicitar contraseña al usuario
contrasena_usuario = input("Ingrese la contraseña: ")

# Verificar coincidencia
if contrasena_usuario == contrasena_correcta:
    print("ACCESO PERMITIDO") 
    print("BIENVENIDO")
else:
    print("Contraseña incorrecta")
    print("ACCESO DENEGADO")