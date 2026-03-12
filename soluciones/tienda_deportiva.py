productos = {}
for i in range(1, 6):
    name = input("Ingresa el nombre del producto: ")
    precio = int(input("Ingresa el precio: "))
    productos[name] = precio

productos_caros = [p for p in productos if productos[p] > 100000]

if productos_caros:
    print("Los siguientes productos tienen un precio mayor a 100000:")
    print("-> " + "\n-> ".join(productos_caros))
else:
    print("No hay productos con precio mayor a 100000.")
