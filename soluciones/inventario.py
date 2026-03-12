agotado = 0
bajo = 0
normal = 0

for i in range(1, 11):

    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad disponible: "))

    if cantidad == 0:
        agotado += 1
    elif cantidad <= 5:
        bajo += 1
    else:
        normal += 1

print("\nEstado del inventario")

print(f"Agotados -> {agotado}")
print(f"Stock bajo -> {bajo}")
print(f"Stock normal -> {normal}")
