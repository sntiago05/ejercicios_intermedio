servicios = {"corte": 0, "cepillado": 0, "tintura": 0}
total_dia = 0

for i in range(1, 8):
    print(f"Cliente {i}")

    nombre = input("Nombre: ")
    servicio = input("Servicio (corte, cepillado, tintura): ").strip().lower()
    valor = int(input("Valor pagado: "))

    total_dia += valor

    if servicio in servicios:
        servicios[servicio] += 1

print(f"\nTotal del dia -> {total_dia}")

print("\nClientes por servicio")
print("\n".join(f"{s} -> {servicios[s]}" for s in servicios))

mas_solicitado = max(servicios, key=servicios.get)  # type: ignore

print(f"Servicio mas solicitado -> {mas_solicitado}")
