cantidad_clientes = 0
productos = {"cono": 3000, "vaso": 4000, "banana split": 9000}
pedidos = {"cono": 0, "vaso": 0, "banana split": 0}
print(
    f"{"\n".join(f'{i+1} -> {s}, precio -> {productos[s]}'for i , s in enumerate(productos))}"
)
continuar = input("Deseas hacer un pedido (si o no)").strip().lower()
while continuar == "si":
    cantidad_clientes += 1
    name = input("Ingresa que producto quieres agregar")
    cantidad = int(input(f"Cuantos {name}s deseas añadir?"))
    if name in pedidos:
        pedidos[name] += cantidad

print(f"total de clientes {cantidad_clientes}")
print(f"total vendido {sum(pedidos[p] * productos[p] for p in pedidos)}")

mas_vendido = max(pedidos, key=pedidos.get)  # type: ignore
print(f"El producto mas vendido fue {mas_vendido}")
