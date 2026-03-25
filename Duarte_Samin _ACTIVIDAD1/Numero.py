# Programa que determina si un número es par o impar

# Solicitar número
numero = int(input("Ingrese un número entero: "))

# Verificar si es par o impar
if numero % 2 == 0:
    print("El número es PAR")
else:
    print("El número es IMPAR")