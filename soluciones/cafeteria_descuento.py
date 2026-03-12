productos = {"cafe": 4000, "capuchino": 7000, "pastel": 6000}

total_dia = 0
numero_cliente = 1

continuar = input("Deseas ingresar pedido? (si / no): ").strip().lower()

while continuar == "si":
    total_cliente = 0
    print(f"\nNuevo cliente {numero_cliente}")

    continuar_cliente = ""

    while continuar_cliente != "salir":
        print(
            "\n".join(
                f"{i+1}. {name} -> {productos[name]}"
                for i, name in enumerate(productos)
            )
        )

        pedido = input("Escoge que pedir: ").strip().lower()

        if pedido in productos:
            total_cliente += productos[pedido]
        else:
            print("Producto no válido")

        continuar_cliente = (
            input("Escribe 'salir' para dejar de pedir: ").strip().lower()
        )

    if total_cliente > 20000:
        total_cliente *= 0.9

    print(f"Total del cliente {numero_cliente} -> {total_cliente}")

    numero_cliente += 1
    total_dia += total_cliente

    continuar = input("Deseas ingresar otro pedido? (si / no): ").strip().lower()

print(f"\nTotal del dia fue: {total_dia}")
