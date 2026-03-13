vehiculos = []
HORA_CARRO = 4000
HORA_MOTO = 2000
for i in range(1, 9):
    print(f"vehiculo {i}")
    placa = input("Ingresa la placa del vehiculo:")
    tipo = input("Ingresa el tipo (carro o moto):")
    horas = int(input("Cuantas horas estuvo parqueado?: "))
    vehiculos.append({"placa": placa, "tipo": tipo, "horas": horas})

print(
    f"total recaudado {sum((HORA_CARRO if v["tipo"] == "carro" else HORA_MOTO)* v["horas"] for v in vehiculos)}"
)

print(f"Total de carros: {sum(1 for c in vehiculos if c["tipo"]== "carro")}")
print(f"Total de motos: {sum(1 for c in vehiculos if c["tipo"]== "moto")}")
mas_pago = max(
    vehiculos,
    key=lambda v: (HORA_CARRO if v["tipo"] == "carro" else HORA_MOTO) * v["horas"],
)

pago = (HORA_CARRO if mas_pago["tipo"] == "carro" else HORA_MOTO) * mas_pago["horas"]

print(
    f"Vehiculo que mas pago -> placa: {mas_pago['placa']} | tipo: {mas_pago['tipo']} | total: {pago}"
)
