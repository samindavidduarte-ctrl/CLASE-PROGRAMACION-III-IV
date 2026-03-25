# Programa que solicita datos personales y muestra su valor y tipo

# Solicitar datos
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura en metros:"))
es_estudiante = input("¿Es estudiante? (Sí/No): ")

#Confirmar si es o no estudiante
if es_estudiante:
    respuesta_estudiante = "Sí"
else:
    respuesta_estudiante = "No"

# Mostrar datos
print("\nDATOS INGRESADOS:")
print("Nombre:", nombre)
print("Edad:", edad,"años")
print("Estatura:", estatura,"metros")
print("Estudiante?:", respuesta_estudiante)