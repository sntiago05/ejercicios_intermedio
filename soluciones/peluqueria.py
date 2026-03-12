hora = int(input("Ingresa la hora de llegada (0hrs - 23hrs): "))
if 6 <= hora <= 11:
    print("Mañana")
elif 12 <= hora <= 17:
    print("tarde")
elif 18 <= hora <= 22:
    print("noche")
else:
    print("fuera de horario")
