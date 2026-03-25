# Programa que solicita cinco notas y calcula el promedio final

# Solicitar cinco notas al usuario
nota1 = float(input("Por favor ingrese la primera nota: "))
nota2 = float(input("Por favor ingrese la segunda nota: "))
nota3 = float(input("Por favor ingrese la tercera nota: "))
nota4 = float(input("Por favor ingrese la cuarta nota: "))
nota5 = float(input("Por favor ingrese la quinta nota: "))

# Calcular el promedio
promedio_final = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

# Mostrar resultado
print("El promedio final es:", promedio_final)