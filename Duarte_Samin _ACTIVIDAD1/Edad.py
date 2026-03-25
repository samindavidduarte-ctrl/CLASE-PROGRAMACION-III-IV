# Programa que determina si una persona puede votar según su edad

# Solicitar edad
edad_usuario = int(input("Por favor ingrese su edad: "))

# Verificar mayoría de edad
if edad_usuario >= 18:
    print("Es mayor de edad y puede votar")
else:
    print("No puede votar, es menor de edad")