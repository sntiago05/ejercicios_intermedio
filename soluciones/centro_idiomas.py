niveles = {"bajo": 0, "medio": 0, "alto": 0}

total_promedios = 0
total_estudiantes = int(input("Cantidad de estudiantes: "))

mejor_estudiante = ""
mejor_promedio = 0

for i in range(1, total_estudiantes + 1):

    nombre = input("Nombre: ")
    speaking = float(input("Nota speaking: "))
    listening = float(input("Nota listening: "))
    reading = float(input("Nota reading: "))

    promedio = (speaking + listening + reading) / 3

    total_promedios += promedio

    if promedio < 60:
        niveles["bajo"] += 1
    elif promedio < 80:
        niveles["medio"] += 1
    else:
        niveles["alto"] += 1

    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_estudiante = nombre

promedio_general = total_promedios / total_estudiantes

print(f"\nPromedio general -> {promedio_general}")
print(f"Mejor estudiante -> {mejor_estudiante} ({mejor_promedio})")

print("\nEstudiantes por nivel")
print("\n".join(f"{n} -> {niveles[n]}" for n in niveles))
