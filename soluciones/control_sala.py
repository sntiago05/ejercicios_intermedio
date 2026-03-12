estado = {"total": 0, "niños": 0, "adultos": 0, "adultos mayores": 0}

capacidad = int(input("Ingresa la capacidad de la sala: "))

while estado["total"] < capacidad:

    continuar = input("Deseas ingresar (si o no): ").strip().lower()
    if continuar == "no":
        break

    edad = int(input("Ingresa tu edad: "))

    estado["total"] += 1

    if edad < 18:
        estado["niños"] += 1
    elif 18 <= edad <= 54:
        estado["adultos"] += 1
    else:
        estado["adultos_mayores"] += 1


print("Sala llena" if estado["total"] == capacidad else "No se llenó la sala")

print("\n".join(f"{k} -> {v}" for k, v in estado.items()))