# Calificaciones del Salón

# Solicitar cantidad de estudiantes
cantidad_estudiantes = int(input("¿Cuántos estudiantes hay en el salón?: "))

aprobados = 0
reprobados = 0

# Ciclo para pedir notas
for i in range(1, cantidad_estudiantes + 1):
    nota = float(input(f"Ingrese la nota del estudiante {i} (0 - 100): "))

    if nota >= 60:
        aprobados += 1
    else:
        reprobados += 1

# Resultados
print("\nResultados:")
print("Estudiantes aprobados:", aprobados)
print("Estudiantes reprobados:", reprobados)