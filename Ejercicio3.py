#Cajero de Productos

cantidad_productos = int(input("¿Cuántos productos desea comprar?: "))

total_pagar = 0

for i in range(1, cantidad_productos + 1):
    precio = float(input(f"Ingrese el precio del producto {i}: $"))

    if precio > 100000:
        descuento = precio * 0.10
        precio_final = precio - descuento
        print(f"Producto {i} tiene descuento del 10%. Precio final: ${precio_final:.2f}")
    else:
        precio_final = precio
        print(f"Producto {i} sin descuento. Precio: ${precio_final:.2f}")

    total_pagar += precio_final

print("\nTotal a pagar: $", round(total_pagar, 2))