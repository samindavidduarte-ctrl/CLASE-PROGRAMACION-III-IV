
#Números Pares e Impares

n = int(input("Ingrese un número entero positivo: "))

pares = 0
impares = 0

for numero in range(1, n + 1):
    if numero % 2 == 0:
        print(numero, "es PAR")
        pares += 1
    else:
        print(numero, "es IMPAR")
        impares += 1 

print("\nTotal de números pares:", pares)
print("Total de números impares:", impares)