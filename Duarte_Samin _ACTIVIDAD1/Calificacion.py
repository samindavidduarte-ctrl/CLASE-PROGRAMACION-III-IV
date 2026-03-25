# Programa que determina si una calificación es aprobatoria

# Solicitar calificación
calificacion = float(input("Ingrese una calificación entre 0 y 100: "))

# Verificar aprobación
if calificacion >= 61:
    print("Aprueba la materia")
elif calificacion >= 60:
    print("Pasó arrastrado, pero aprueba")
else:
    print("No aprueba la materia")
    