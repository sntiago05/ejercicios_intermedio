planes = {
    "basico": 50000,
    "premium": 90000,
    "familiar": 130000
}

conteo_planes = {"basico": 0, "premium": 0, "familiar": 0}

total = 0

personas = int(input("Cuantas personas se registran: "))

for i in range(1, personas + 1):

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    plan = input("Tipo de plan (basico, premium, familiar): ").strip().lower()

    if plan in planes:
        total += planes[plan]
        conteo_planes[plan] += 1

    if edad < 18:
        print("registro juvenil")

    if edad >= 60:
        print("beneficio senior")

print(f"\nTotal recaudado -> {total}")

print("\nPersonas por plan")
print("\n".join(f"{p} -> {conteo_planes[p]}" for p in conteo_planes))

mas_vendido = max(conteo_planes, key=conteo_planes.get) # type: ignore

print(f"Plan mas vendido -> {mas_vendido}")